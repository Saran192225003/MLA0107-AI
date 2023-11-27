import itertools
import sys

def calculate_distance(city1, city2):
    return distances[city1][city2]

def nearest_neighbor_algorithm(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    tour = []

    current_city = 0
    tour.append(current_city)

    while len(tour) < num_cities:
        nearest_city = min(
            (city for city in cities if city not in tour),
            key=lambda city: distances[current_city][city]
        )
        tour.append(nearest_city)
        current_city = nearest_city

    tour.append(tour[0])  # Return to the starting city to complete the tour
    return tour

# Example usage:
if __name__ == "__main__":
    # Example distances between cities (replace with your own data)
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    # Find the tour using the nearest neighbor algorithm
    tour = nearest_neighbor_algorithm(distances)

    # Print the tour and total distance
    print("Shortest Tour:", tour)
    total_distance = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    print("Total Distance:", total_distance)
