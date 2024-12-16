
from point import Point
from drawer import Drawer
from fastest_descent import fastest_descent

if __name__ == '__main__':
  result = fastest_descent(0.01, -1, 4)
  point = Point(result[0][0], result[1][0])
  drawer = Drawer(point)
