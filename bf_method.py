import func_declaration
from point import Point
from scipy.optimize import _minimize as optimize
from math import log

def barrier_function(x0: Point, r0: float, c: float, eps: float) -> tuple[Point, int]:
    rk = r0
    k: int = 0
    xk: Point = x0
    while True:
        def p(var: list, rk: float) -> float:
            return -rk * log(-func_declaration.g1(var))
        def fxrk(var: list) -> float:
            return func_declaration.f(var) + p(var, rk)
        x_min = optimize.minimize(fxrk, [xk.x, xk.y])
        x_point = Point(x_min.x[0], x_min.x[1])
        tmp = p([x_point.x, x_point.y], rk)
        if abs(tmp) <= eps:
            return [x_point, k]
        else:
            rk = rk / c
            xk = x_point
            k = k + 1