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
        a_cmd = self.coxa_offset + self.coxa_sign * a
        b_cmd = self.femur_offset + self.femur_sign * b
        c_cmd = self.tibia_offset + self.tibia_sign * c

        a_cmd = self.clamp(a_cmd, self.coxa_min, self.coxa_max)
        b_cmd = self.clamp(b_cmd, self.femur_min, self.femur_max)
        c_cmd = self.clamp(c_cmd, self.tibia_min, self.tibia_max)

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

        self.set_joint_angles(a, b, c)


class Hexapod:
    def __init__(self, legs):
        self.legs = legs

        # tripod gait phase offsets
        self.phase_offsets = [
            0.0 if i in (0, 2, 4) else 0.5
            for i in range(len(legs))
        ]

        # current gait settings
        self.step_length = 20
        self.step_height = 10
        self.ground_z = -50
        self.walk_period = 1.0

        # stop handling
        self.stop_requested = False
        self.is_standing = True

    def _global_phase(self, time_now, period):
        return (time_now % period) / period

    def _at_cycle_boundary(self, global_phase, tol=0.05):
        return global_phase < tol or global_phase > (1.0 - tol)

    def request_stop(self):
        """
        Request a stop at the end of the current gait cycle.
        """
        self.stop_requested = True

    def clear_stop_request(self):
        self.stop_requested = False
        self.is_standing = False

    def stand(self):
        for leg in self.legs:
            leg.move_foot(leg.home_x, leg.home_y, leg.home_z)
        self.is_standing = True

    def sit(self):
        for leg in self.legs:
            x = leg.home_x
            y = leg.home_y
            z = leg.home_z + 20   # less negative = body lower / legs less extended
            leg.move_foot(x, y, z)
        self.is_standing = False

    def walk_forward(self, time_now, step_length=20, step_height=10, ground_z=-50, period=1.0):
        self.step_length = step_length
        self.step_height = step_height
        self.ground_z = ground_z
        self.walk_period = period

        global_phase = self._global_phase(time_now, period)

        # if stop requested, only stop when current cycle reaches boundary
        if self.stop_requested and self._at_cycle_boundary(global_phase):
            self.stand()
            return

        self.is_standing = False

        for i, leg in enumerate(self.legs):
            leg_phase = (global_phase + self.phase_offsets[i]) % 1.0

            x, y, z = leg.foot_trajectory(
                leg_phase,
                step_length,
                step_height,
                ground_z
            )

            leg.move_foot(x, y, z)

    def turn_left(self, time_now, turn_amount=1.0, step_height=10, ground_z=-50, period=1.0):
        """
        Simple turning gait:
        - right legs take a larger forward/back step
        - left legs take a smaller / reversed step
        - same tripod timing as walking

        Assumes leg indices:
            0,1,2 = right side
            3,4,5 = left side
        """
        turn_amount = max(0.0, min(1.0, turn_amount))

        self.step_height = step_height
        self.ground_z = ground_z
        self.walk_period = period

        global_phase = self._global_phase(time_now, period)

        if self.stop_requested and self._at_cycle_boundary(global_phase):
            self.stand()
            return

        self.is_standing = False

        base_step = 20
        outer_step = base_step * (1.0 + turn_amount)
        inner_step = base_step * (1.0 - turn_amount)

        for i, leg in enumerate(self.legs):
            leg_phase = (global_phase + self.phase_offsets[i]) % 1.0

            is_left = (i >= 3)

            # turning left:
            # right side pushes more forward/back
            # left side pushes less, or slightly opposite for tighter turn
            if is_left:
                local_step = -0.5 * inner_step
            else:
                local_step = outer_step

            x, y, z = leg.foot_trajectory(
                leg_phase,
                local_step,
                step_height,
                ground_z
            )

            leg.move_foot(x, y, z)

    def update_stopping_gait(self, time_now):
        """
        Keep running the last gait until it reaches a safe stop boundary.
        Use this when stop has been requested.
        """
        global_phase = self._global_phase(time_now, self.walk_period)

        if self._at_cycle_boundary(global_phase):
            self.stand()
            return

        # continue previous walk settings while stopping
        self.walk_forward(
            time_now,
            step_length=self.step_length,
            step_height=self.step_height,
            ground_z=self.ground_z,
            period=self.walk_period
        )
        
    def turn_right(self, time_now, turn_amount=1.0, step_height=10, ground_z=-50, period=1.0):
        """
        Turning right gait (mirror of turn_left).

        - left legs take bigger forward/back steps
        - right legs take smaller / reversed steps

        Assumes leg indices:
            0,1,2 = right side
            3,4,5 = left side
        """

        turn_amount = max(0.0, min(1.0, turn_amount))

        self.step_height = step_height
        self.ground_z = ground_z
        self.walk_period = period

        global_phase = self._global_phase(time_now, period)

        # allow graceful stop
        if self.stop_requested and self._at_cycle_boundary(global_phase):
            self.stand()
            return

        self.is_standing = False

        base_step = 20
        outer_step = base_step * (1.0 + turn_amount)
        inner_step = base_step * (1.0 - turn_amount)

        for i, leg in enumerate(self.legs):

            leg_phase = (global_phase + self.phase_offsets[i]) % 1.0

            is_left = (i >= 3)

            # turning RIGHT → LEFT legs push more
            if is_left:
                local_step = outer_step
            else:
                local_step = -0.5 * inner_step

            x, y, z = leg.foot_trajectory(
                leg_phase,
                local_step,
                step_height,
                ground_z
            )

            leg.move_foot(x, y, z)