import math
import matplotlib.pyplot as plt

# abcd matrix to use for 1m propagation, 0.25m thin lens, 1m propagation: -3, -2, -4, -3
abcd = [-3, -2, -4, -3]

r1 = [.01, .08] # m, rad

def propagate(abcd: list, r: list) -> list:
    x = abcd[0] * r[0] + abcd[1] * r[1]
    y = abcd[2] * r[0] + abcd[3] * r[1]

    return [x, y]

r2 = propagate(abcd, r1)

r1 = [[0, 0], r1]
r2 = [[2, 0], r2]

def tovec(ray: list) -> list: # [position, angle]
    print(ray)
    x = math.cos(ray[1]) * ray[0]
    y = math.sin(ray[1]) * ray[0]

    return [x, y]

def visualize(rays: list):
    plt.title("Unit vector rays for propagation through a thin lens")
    plt.xlabel('z (m)')
    plt.ylabel('y (m)')

    for ray in rays:
        ray[1] = tovec(ray[1])
        print(ray)

    for ray in rays:
        plt.quiver(ray[0][0], ray[0][1], ray[1][0], ray[1][1])

    # Add a simple lens in the middle
    plt.plot([1, 1], [-.1, .1], color='black')

    plt.show()

visualize([r1, r2])