from workout import WorkoutOne, WorkoutTwo, WorkoutThree, WorkoutFour


class Microcycle:

    """A month of workouts."""

    def __init__(self, squat_1rm, deadlift_1rm, bench_1rm, press_1rm):
        self.squat_1rm = squat_1rm
        self.deadlift_1rm = deadlift_1rm
        self.bench_1rm = bench_1rm
        self.press_1rm = press_1rm

    def get_workout(self, workout_number):
        if workout_number == 1:
            return WorkoutOne()
        elif workout_number == 2:
            return WorkoutTwo()
        elif workout_number == 3:
            return WorkoutThree()
        elif workout_number == 4:
            return WorkoutFour()
