import func_declaration
from point import Point
from scipy.optimize import _minimize as optimize

def penalty_method(x0: Point, r0: float, c: float, eps: float) -> tuple[Point, int]:
    rk = r0
    k: int = 0
    xk: Point = x0
    while True:
        def p(var: list, rk: float) -> float:
            return (rk / 2) * pow(func_declaration.g1(var), 2)
        def fxrk(var: list) -> float:
            return func_declaration.f(var) + p(var, rk)
        x_min = optimize.minimize(fxrk, [xk.x, xk.y])
        x_point = Point(x_min.x[0], x_min.x[1])
        tmp = p([x_point.x, x_point.y], rk)
        if tmp <= eps:
            return [x_point, k]
        else:
            rk = c * rk
            xk = x_point
            k = k + 1