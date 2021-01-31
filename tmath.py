import math


def magn(x, y):
    value = math.sqrt(x*x + y*y)
    return 1.0 if value == 0.0 else value

def dist(ax, ay, bx, by):
    return magn(bx - ax, by - ay)


def dot(ax, ay, bx, by):
    return ax*bx + ay*by


def angle(ax, ay, bx, by):
    dx = bx - ax
    dy = by - ay
    return math.degrees(math.acos(dot(dx, dy, 1.0, 0.0)/magn(dx, dy)))*(-1 if dot(dx, dy, 0.0, 1.0) > 0 else 1)


def orientation(ax, ay, bx, by):
    value = angle(ax, ay, bx, by)
    return (
        0 if (-0.1 < value < 0.1) else (
            1 if (58 < value < 62) else (
                2 if (118 < value < 122) else (
                    3 if (178 < value < 182) else (
                        4 if (-122 < value < -118) else (
                            5 if (-62 < value < -58) else -1
                        )
                    )
                )
            )
        )
    )


def check_60(ax, ay, bx, by):
    value = abs(angle(ax, ay, bx, by))
    return (value < 0.1) or (58.0 < value < 62.0) or (118.0 < value < 122.0) or (178.0 < value < 182.0)