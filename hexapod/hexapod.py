class Leg:
    def __init__(self, coxa, femur, tibia, config):
        self.coxa = coxa # servo for horizontal rotation
        self.femur = femur # servo for vertical movement of the upper leg
        self.tibia = tibia # servo for vertical movement of the lower leg 
        self.config = config # configuration for the leg, such as lengths of segments

    def set_joint_angles(self, a, b, c): # set angles for coxa, femur, tibia respectively
        pass

    
    def foot_trajectory(self, phase, step_length, step_height, ground_z):
        """
        Generate desired foot position for walking gait.

        Parameters
        ----------
        phase : float (0 → 1)
            Normalised step cycle phase.
            0.0 = start of step
            0.5 = mid step
            1.0 = end of step (wraps to 0)

        step_length : float
            How far forward/back the foot moves.

        step_height : float
            Maximum height of foot during swing phase.

        ground_z : float
            Nominal ground contact height (negative = below body).

        Returns
        -------
        (x, y, z) : tuple
            Desired foot position in leg coordinate frame.
        """

        # ---- Swing phase (foot in air) ----
        # Usually first half of cycle
        if phase < 0.5:

            # map phase 0→0.5 into swing progress 0→1
            u = phase / 0.5

            # TODO:
            # move foot from rear to front
            # example idea: linear interpolation
            x = None  # replace with: rear_position + step_length * u

            # TODO:
            # lift foot using smooth curve
            # example: sinusoidal arc
            z = None  # replace with: ground_z + step_height * sin(pi * u)

        # ---- Stance phase (foot on ground pushing robot) ----
        else:

            # map phase 0.5→1 into stance progress 0→1
            u = (phase - 0.5) / 0.5

            # TODO:
            # move foot from front back to rear
            # this simulates body moving forward over planted foot
            x = None  # replace with: front_position - step_length * u

            # foot stays on ground
            z = ground_z

        # TODO:
        # lateral offset depending on leg mounting position
        y = None  # often constant per leg

        return x, y, z

    def move_foot(self, x, y, z):
        """
        Convert desired foot position into servo joint angles.

        Steps typically involved:

        1) Transform (x, y, z) into leg coordinate frame
           - account for body rotation / translation
           - account for leg mounting angle

        2) Solve inverse kinematics
           - compute coxa angle from horizontal projection
           - compute femur & tibia using triangle geometry

        3) Apply calibration offsets
           - servo neutral angle shifts
           - mechanical mounting differences

        4) Clamp to safe joint limits
           - avoid self collision
           - avoid servo overtravel

        5) Send commands to servos
        """

        # TODO:
        # compute coxa_angle
        coxa_angle = None

        # TODO:
        # compute femur_angle
        femur_angle = None

        # TODO:
        # compute tibia_angle
        tibia_angle = None

        # TODO:
        # send angles to hardware
        # self.set_joint_angles(coxa_angle, femur_angle, tibia_angle)

        pass

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

        High-level process:
        1) compute global gait phase from time
        2) shift phase for each leg using its phase offset
        3) ask each leg for desired foot trajectory
        4) command each leg to move to that position
        """

        # TODO:
        # convert time into cycle phase from 0 to 1
        global_phase = None

        for i, leg in enumerate(self.legs):

            # TODO:
            # apply per-leg phase offset
            leg_phase = None

            # TODO:
            # get desired foot position for this phase
            x, y, z = leg.foot_trajectory(
                leg_phase,
                step_length,
                step_height,
                ground_z
            )

            # TODO:
            # for real robot, may need to add per-leg lateral offset here
            # or apply body-frame to leg-frame transform

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