import math

class Leg:
    def __init__(
        self,
        coxa, femur, tibia,
        L1, L2, L3,
        home_x=50, home_y=0, home_z=-40,

        coxa_offset=90, femur_offset=90, tibia_offset=90,
        coxa_sign=1, femur_sign=1, tibia_sign=1,

        coxa_min=0, coxa_max=180,
        femur_min=0, femur_max=180,
        tibia_min=0, tibia_max=180
    ):
        self.coxa = coxa
        self.femur = femur
        self.tibia = tibia

        self.L1 = L1
        self.L2 = L2
        self.L3 = L3

        self.home_x = home_x
        self.home_y = home_y
        self.home_z = home_z

        self.coxa_offset = coxa_offset
        self.femur_offset = femur_offset
        self.tibia_offset = tibia_offset

        self.coxa_sign = coxa_sign
        self.femur_sign = femur_sign
        self.tibia_sign = tibia_sign

        self.coxa_min = coxa_min
        self.coxa_max = coxa_max
        self.femur_min = femur_min
        self.femur_max = femur_max
        self.tibia_min = tibia_min
        self.tibia_max = tibia_max

    def clamp(self, value, low, high):
        return max(low, min(high, value))

    def set_joint_angles(self, a, b, c):
        """
        a, b, c are IK angles in degrees.
        Convert them to servo command angles with offset/sign.
        """

        a_cmd = self.coxa_offset + self.coxa_sign * a
        b_cmd = self.femur_offset + self.femur_sign * b
        c_cmd = self.tibia_offset + self.tibia_sign * c

        a_cmd = self.clamp(a_cmd, self.coxa_min, self.coxa_max)
        b_cmd = self.clamp(b_cmd, self.femur_min, self.femur_max)
        c_cmd = self.clamp(c_cmd, self.tibia_min, self.tibia_max)

        print(
            f"CMD angles: coxa={a_cmd:.1f}, femur={b_cmd:.1f}, tibia={c_cmd:.1f}"
        )

        self.coxa.move_to_angle(a_cmd)
        self.femur.move_to_angle(b_cmd)
        self.tibia.move_to_angle(c_cmd)

    def foot_trajectory(self, phase, step_length, step_height, ground_z):
        phase = phase % 1.0

        x = self.home_x

        if phase < 0.5:
            s = phase / 0.5
            y = self.home_y + (step_length / 2) * (1 - 2 * s)
            z = ground_z
        else:
            s = (phase - 0.5) / 0.5
            y = self.home_y + (-step_length / 2 + step_length * s)
            z = ground_z + step_height * (4 * s * (1 - s))

        return x, y, z

    def move_foot(self, x, y, z):
        theta1 = math.atan2(y, x)

        H = math.sqrt(x**2 + y**2)
        Y = H - self.L1
        L = math.sqrt(Y**2 + z**2)

        max_reach = self.L2 + self.L3
        min_reach = abs(self.L2 - self.L3)

        if L > max_reach:
            L = max_reach
        if L < min_reach:
            L = min_reach

        c3 = (self.L2**2 + self.L3**2 - L**2) / (2 * self.L2 * self.L3)
        c3 = max(-1.0, min(1.0, c3))
        theta3 = math.acos(c3)

        if L == 0:
            return

        cb = (L**2 + self.L2**2 - self.L3**2) / (2 * self.L2 * L)
        cb = max(-1.0, min(1.0, cb))
        beta = math.acos(cb)

        alpha = math.atan2(z, Y)
        theta2 = beta - alpha

        a = math.degrees(theta1)
        b = math.degrees(theta2)
        c = math.degrees(theta3)

        print(
            f"IK for foot ({x:.1f}, {y:.1f}, {z:.1f}): "
            f"theta1={a:.1f}, theta2={b:.1f}, theta3={c:.1f}"
        )

        self.set_joint_angles(a, b, c)

class Hexapod:

    def __init__(self, legs):
        self.legs = legs

        # TODO:
        # define which legs belong to each tripod group
        # example idea:
        # tripod A = legs 0, 3, 4
        # tripod B = legs 1, 2, 5
        self.phase_offsets = [None] * len(legs)

        # TODO:
        # store current gait / motion settings
        self.step_length = 0
        self.step_height = 0
        self.ground_z = 0
        self.walk_period = 1.0

    def stand(self):
        """
        Move all legs to a neutral standing pose.

        Typical steps:
        1) choose a default foot position for each leg
        2) send each leg to that position
        3) make sure body is balanced and symmetric
        """

        for leg in self.legs:
            # TODO:
            # choose default standing foot position
            x = None
            y = None
            z = None

            # command leg to that position
            leg.move_foot(x, y, z)

    def sit(self):
        """
        Move robot into a lower resting pose.

        Typical idea:
        - keep feet roughly under body
        - reduce body height by changing z
        """

        for leg in self.legs:
            # TODO:
            # choose lower foot/body position
            x = None
            y = None
            z = None

            leg.move_foot(x, y, z)

    def walk_forward(self, time_now, step_length=20, step_height=10, ground_z=-50, period=1.0):
        """
        Update all legs for forward walking based on current time.

        Parameters
        ----------
        time_now : float
            Current time in seconds or ticks converted to seconds.

        step_length : float
            Forward/back reach of each step.

        step_height : float
            Foot lift height during swing phase.

        ground_z : float
            Nominal ground level relative to body.

        period : float
            Time for one full gait cycle.
        """

        # Convert time into repeating phase from 0.0 to 1.0
        global_phase = (time_now % period) / period

        for i, leg in enumerate(self.legs):

            # Simple tripod gait:
            # legs 0, 2, 4 in one tripod
            # legs 1, 3, 5 in the other tripod
            phase_offset = 0.0 if i in (0, 2, 4) else 0.5

            # Shift phase for this leg and wrap back into [0, 1)
            leg_phase = (global_phase + phase_offset) % 1.0

            # Ask leg for target foot position
            x, y, z = leg.foot_trajectory(
                leg_phase,
                step_length,
                step_height,
                ground_z
            )

            # Move that leg to the target foot position
            leg.move_foot(x, y, z)

    def turn_left(self, time_now, turn_amount=1.0, step_height=10, ground_z=-50, period=1.0):
        """
        Update all legs for turning left.

        Typical turning idea:
        - left and right legs use different x/y trajectories
        - some legs may step slightly inward/outward
        - body rotates because stance legs push asymmetrically

        This can later reuse the same gait timing as walk_forward(),
        but with different target foot paths.
        """

        # TODO:
        # compute global gait phase
        global_phase = None

        for i, leg in enumerate(self.legs):

            # TODO:
            # apply per-leg phase offset
            leg_phase = None

            # TODO:
            # generate turning-specific foot target
            # could depend on whether leg is on left or right side
            x = None
            y = None
            z = None

            leg.move_foot(x, y, z)

    def stop(self):
        """
        Stop walking and hold current or neutral pose.

        Possible strategies:
        - freeze current foot positions
        - return smoothly to standing pose
        """
        pass