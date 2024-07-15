import numpy as np
import random

# draw a circle to z axis
def draw_circle(radius, num_points):
    points = []
    for i in range(num_points):
        theta = 2 * np.pi * i / num_points
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        points.append([x, y, 2])
    return np.array(points)

points = draw_circle(2, 36)

# draw this points a 3d plane and show with matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(points[:, 0], points[:, 1], points[:, 2])

# show axis x, y, z
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

with open("/YOUR-HOME-PATH/gaussian-splatting/camera_center.txt", "w") as f:
    for point in points:
        f.write(f"{point[0]:.2f} {point[1]:.2f} {point[2]:.2f}\n")





