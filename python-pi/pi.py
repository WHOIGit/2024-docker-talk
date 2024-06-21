import random
import os

def approximate_pi(num_points):
    points_inside_circle = 0
    total_points = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1

        total_points += 1

    pi_approximation = 4 * (points_inside_circle / total_points)
    return pi_approximation

if __name__ == "__main__":
    num_points = int(os.getenv("NUM_POINTS", 100000))
    pi_approximation = approximate_pi(num_points)
    print(pi_approximation)