from point import Point

def f(var: list) -> float:
    p: Point = Point(var[0], var[1])
    return -(p.x - (2 * pow(p.y, 2)) + 4 * p.y)

def g1(var: list) -> float:
    p: Point = Point(var[0], var[1])
    return -((-3 * p.x) - (-2 * p.y) - 6)