import matplotlib.pyplot as plt
import numpy as np

from point import Point
from interval import Interval

class Drawer:
  def __init__(self, point: Point):
    # Задаем начальные настройки для отрисовки.
    self.X, self.Y = np.mgrid[Interval.x_min:Interval.x_max:100j, Interval.y_min:Interval.y_max:100j]
    self.fig = plt.figure(figsize=(10, 10))
    self.ax = self.fig.add_subplot(1, 1, 1, projection='3d')
    self.ax.plot_surface(self.X, self.Y, self.__function(self.X , self.Y), alpha=0.5)
    # Добавляем вычисленную точку на график и отрисовываем сам график.
    self.__add_point(point)
    plt.show()
    pass

  # Заданная функция.
  def __function(self, x1, x2):
    return pow((x1 - 1), 2) + pow((x2 - 3), 2)

  # Приватный метод добавления точки экстремума на график.
  def __add_point(self, point: Point):
    point_computed_by_extremum = self.__function(point.x, point.y)
    self.ax.scatter(point.x, point.y, point_computed_by_extremum, color='red')