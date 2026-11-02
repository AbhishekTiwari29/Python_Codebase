import math

def nearest_neighbor(neighbors, point):

    min_distance = float('inf')
    nearest = None

    for neighbor in neighbors:

        distance = math.sqrt(
            (point[0] - neighbor[0])**2 +
            (point[1] - neighbor[1])**2
        )

        if distance < min_distance:
            min_distance = distance
            nearest = neighbor

    return nearest


neighbors = {(2, 3), (5, 6), (1, 1), (8, 9)}
point = (2, 6)

print("Nearest Neighbor:", nearest_neighbor(neighbors, point))