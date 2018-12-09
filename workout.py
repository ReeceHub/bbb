from exercise import Exercise


class WorkoutOne:

    def __init__(self):
        self.exercises = [
            Exercise('Press', 3 * [5], None),  # TODO: this is only true workout 1 week 1
            Exercise('Bench', 5 * [10], None),
            Exercise('Chins', 5 * [10], None)
        ]


class WorkoutTwo:

    def __init__(self):
        self.exercises = [
            Exercise('Deadlift', 3 * [5], None),
            Exercise('Squat', 5 * [10], None),
            Exercise('AbWheel', 5 * [10], None)  # TODO: want to be able to express 10-20 reps
        ]


class WorkoutThree:

    def __init__(self):
        self.exercises = [
            Exercise('Bench', 3 * [5], None),
            Exercise('Press', 5 * [10], None),
            Exercise('DBRows', 5 * [10], None)
        ]


class WorkoutFour:

    def __init__(self):
        self.exercises = [
            Exercise('Squat', 3 * [5], None),
            Exercise('Deadlift', 5 * [10], None),
            Exercise('HangingLegRaise', 5 * [10], None)
        ]
