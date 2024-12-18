import minimization

import numdifftools as nd
import numpy as np
from typing import Callable

def fastest_descent(func: Callable, tolerance: float, start_x: float, start_y: float):
    starting_point = np.array([[start_x], [start_y]])

    relaxation_sequence = []
    function_values = []
    calculated_values: int = 0
    iterations: int = 0

    relaxation_sequence.append(starting_point)
    iterations += 1

    function_values.append(func([starting_point[0][0], starting_point[1][0]]))

    df = nd.Gradient(func)

    gradient = np.array([[1.], [1.]])

    while ((gradient[0][0]**2) + (gradient[1][0]**2))**0.5 > tolerance:
        current_point = relaxation_sequence[iterations-1]

        gradient[0][0], gradient[1][0] = df([current_point[0][0], current_point[1][0]])
        calculated_values += 2

        def psi(xi):
            x = current_point[0][0] + (-1)*gradient[0][0]*abs(xi)
            y = current_point[1][0] + (-1)*gradient[1][0]*abs(xi)
            return func([x, y])
        
        golden_tolerance = 0.0001
        golden_data = minimization.golden(f=psi, a=0., b=0.1, tolerance=golden_tolerance)
        xi = abs(golden_data[0])
        calculated_values += golden_data[1]

        new_point = np.array([[0.], [0.]])
        new_point[0][0] = current_point[0][0] + (-1)*gradient[0][0]*xi
        new_point[1][0] = current_point[1][0] + (-1)*gradient[1][0]*xi
        relaxation_sequence.append(new_point)
        iterations += 1

        function_values.append(func([new_point[0][0], new_point[1][0]]))

    print(iterations, relaxation_sequence[iterations-1])
    return relaxation_sequence[iterations-1]
