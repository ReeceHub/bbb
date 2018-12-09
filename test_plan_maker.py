from plan_maker import PlanMaker
from microcycle import Microcycle


class TestPlanMakerInit:

    def test_initialisation(self):
        pm = PlanMaker(squat=1, deadlift=2, bench=3, press=4)

        assert pm.squat_start == 1
        assert pm.deadlift_start == 2
        assert pm.bench_start == 3
        assert pm.press_start == 4

    def test_first_month_1rm(self):
        pm = PlanMaker(squat=1, deadlift=2, bench=3, press=4)

        assert pm.squat_1rm(1) == 1
        assert pm.deadlift_1rm(1) == 2
        assert pm.bench_1rm(1) == 3
        assert pm.press_1rm(1) == 4

    def test_second_month_1rm(self):
        pm = PlanMaker(squat=1, deadlift=2, bench=3, press=4)

        # up by 5
        assert pm.squat_1rm(2) == 6
        assert pm.deadlift_1rm(2) == 7

        # up by 2.5
        assert pm.bench_1rm(2) == 5.5
        assert pm.press_1rm(2) == 6.5

    def test_tenth_month_1rm(self):
        pm = PlanMaker(squat=1, deadlift=2, bench=3, press=4)

        # up by 5 each month
        assert pm.squat_1rm(10) == 1 + (9 * 5)
        assert pm.deadlift_1rm(10) == 2 + (9 * 5)

        # up by 2.5 each month
        assert pm.bench_1rm(10) == 3 + (9 * 2.5)
        assert pm.press_1rm(10) == 4 + (9 * 2.5)

    def test_overriding_monthly_increment(self):
        pm = PlanMaker(squat=1, deadlift=2, bench=3, press=4, increment=20)

        # up by 20
        assert pm.squat_1rm(2) == 21
        assert pm.deadlift_1rm(2) == 22

        # up by 10
        assert pm.bench_1rm(2) == 13
        assert pm.press_1rm(2) == 14


class TestMicrocycleCreation:

    def test_microcycle_can_be_made(self):
        mc = PlanMaker().make_microcycle(1)

        assert isinstance(mc, Microcycle)
        assert mc.squat_1rm == 80
        assert mc.deadlift_1rm == 100
        assert mc.bench_1rm == 50
        assert mc.press_1rm == 30

    def test_microcycle_workouts(self):
        mc = PlanMaker().make_microcycle(1)

        assert len(mc.workouts) == 4
