class Microcycle:

    """A month of workouts."""

    def __init__(self, squat_1rm, deadlift_1rm, bench_1rm, press_1rm):
        self.squat_1rm = squat_1rm
        self.deadlift_1rm = deadlift_1rm
        self.bench_1rm = bench_1rm
        self.press_1rm = press_1rm
        self.workouts = ['w1', 'w2', 'w3', 'w4']
