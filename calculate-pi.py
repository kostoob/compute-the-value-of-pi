import random

def compute_pi(n):
    points_in_circle = 0
    points_in_square = 0
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            points_in_circle += 1
        points_in_square += 1
    pi = (points_in_circle*4)/points_in_square
    print(pi)


compute_pi(100)
