from penalty_method import penalty_method
from point import Point
from drawer import Drawer
from fastest_descent import fastest_descent
import func_declaration

if __name__ == '__main__':
  #result = fastest_descent(0.01, -1, 4)
  #point = Point(result[0][0], result[1][0])
  ret: tuple[Point, int] = penalty_method(Point(-4, 1), 0.01, 4, 0.001)
  drawer = Drawer(func_declaration.f)
  drawer.AddPlane(func_declaration.g1)
  drawer.AddPoint(ret[0])
  drawer.AddTitle(k = ret[1], extr = ret[0])
  drawer.Show()
