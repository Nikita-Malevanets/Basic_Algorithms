import random

import scipy.integrate as spi


def f(x):
    return x ** 2


def monte_carlo_integration(func, a, b, num_points):
    max_y = func(b)
    points_under_curve = 0

    for _ in range(num_points):
        rand_x = random.uniform(a, b)
        rand_y = random.uniform(0, max_y)

        if rand_y <= func(rand_x):
            points_under_curve += 1

    rectangle_area = (b - a) * max_y
    integral_value = rectangle_area * (points_under_curve / num_points)

    return integral_value


a = 0
b = 2
N = 100_000

mc_result = monte_carlo_integration(f, a, b, N)
quad_result, error = spi.quad(f, a, b)

print(f"Метод Монте-Карло ({N} точок): {mc_result}")
print(f"Метод quad (Scipy): {quad_result}")
print(f"Абсолютна помилка: {abs(mc_result - quad_result)}")
