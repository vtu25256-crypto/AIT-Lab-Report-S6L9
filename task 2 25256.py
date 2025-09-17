import numpy as np
import random

def calculate_total_distance(tour, distances):
    total = 0
    for i in range(len(tour)):
        total += distances[tour[i]][tour[(i + 1) % len(tour)]]  # next city, loop back to start
    return total

def get_neighbors(tour):
    neighbors = []
    for i in range(len(tour)):
        for j in range(i + 1, len(tour)):
            neighbor = tour.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  # swap two cities
            neighbors.append(neighbor)
    return neighbors

def hill_climbing(distances, max_iterations=1000):
    n = len(distances)
    current_tour = list(range(n))
    random.shuffle(current_tour)  # start with random tour
    current_distance = calculate_total_distance(current_tour, distances)

    for _ in range(max_iterations):
        neighbors = get_neighbors(current_tour)
        next_tour = None
        next_distance = current_distance

        for neighbor in neighbors:
            dist = calculate_total_distance(neighbor, distances)
            if dist < next_distance:
                next_tour = neighbor
                next_distance = dist

        if next_tour is None:
            break  # no better neighbor found, local optimum reached

        current_tour = next_tour
        current_distance = next_distance

    return current_tour, current_distance

# Example distances matrix
distances = np.array([
    [0, 2, 2, 5],
    [2, 0, 3, 4],
    [2, 3, 0, 1],
    [5, 4, 1, 0]
])

best_tour, best_distance = hill_climbing(distances)
print("Best tour found:", best_tour)
print("Distance:", best_distance)
