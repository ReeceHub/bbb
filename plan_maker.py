from microcycle import Microcycle


class PlanMaker:

    def __init__(self, squat=80, deadlift=100, bench=50, press=30, increment=5):
        self.squat_start = squat
        self.deadlift_start = deadlift
        self.bench_start = bench
        self.press_start = press
        self.increment = increment

    def squat_1rm(self, month):
        return self.squat_start + (month - 1) * self.increment

    def deadlift_1rm(self, month):
        return self.deadlift_start + (month - 1) * self.increment

    def bench_1rm(self, month):
        return self.bench_start + (month - 1) * (self.increment / 2)

    def press_1rm(self, month):
        return self.press_start + (month - 1) * (self.increment / 2)

    def make_microcycle(self, month):
        return Microcycle(
            self.squat_1rm(month),
            self.deadlift_1rm(month),
            self.bench_1rm(month),
            self.press_1rm(month)
        )
