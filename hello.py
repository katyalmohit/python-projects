import math
n = 15
radius = 0.2/ 2
angle = 2 * math.pi / n
points = [(math.cos(i * angle) * radius, math.sin(i * angle) * radius) for i in range(n)]
print(points)
