from fastest_descent import fastest_descent
from point import Point

def f(var: list) -> float:
    return var[0]**2 + var[1]**2

def g1(var: list) -> float:
    return (-2 * var[0]) - var[1] - 2

def p(var: list, rk: float) -> float:
    return (rk / 2) * (g1(var)**2)

def penalty_method(x0: Point, r0: float, c: float, eps: float) -> Point:
    rk = r0
    k: int = 0
    xk: Point = x0
    while True:
        def fxrk(var: list):
            return f(var) + p(var, rk)
        x_min = fastest_descent(fxrk, eps, xk.x, xk.y)
        x_point = Point(x_min[0][0], x_min[1][0])
        tmp = p([x_point.x, x_point.y], rk)
        if tmp <= eps:
            return x_point
        else:
            rk = c * rk
            xk = x_point
            k = k + 1