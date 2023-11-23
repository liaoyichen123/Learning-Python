# Required Libraries
import numpy as np
import matplotlib.pyplot as plt
from concorde.tsp import TSPSolver
from haversine import haversine

# Define the cities and their coordinates
cities = {
    'New York City': (40.72, -74.00),
    'Philadelphia': (39.95, -75.17),
    'Baltimore': (39.28, -76.62),
    'Charlotte': (35.23, -80.85),
    'Memphis': (35.12, -89.97),
    'Jacksonville': (30.32, -81.70),
    'Houston': (29.77, -95.38),
    'Austin': (30.27, -97.77),
    'San Antonio': (29.53, -98.47),
    'Fort Worth': (32.75, -97.33),
    'Dallas': (32.78, -96.80),
    'San Diego': (32.78, -117.15),
    'Los Angeles': (34.05, -118.25),
    'San Jose': (37.30, -121.87),
    'San Francisco': (37.78, -122.42),
    'Indianapolis': (39.78, -86.15),
    'Phoenix': (33.45, -112.07),
    'Columbus': (39.98, -82.98),
    'Chicago': (41.88, -87.63),
    'Detroit': (42.33, -83.05)
}

# Function to compute the distance matrix
def compute_distance_matrix(cities):
    city_names = list(cities.keys())
    n = len(city_names)
    distance_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i != j:
                city1 = cities[city_names[i]]
                city2 = cities[city_names[j]]
                distance_matrix[i][j] = haversine(city1, city2)

    return distance_matrix

# Compute the distance matrix
distance_matrix = compute_distance_matrix(cities)

# Solve the TSP
lst_xs = []
lst_ys = []
for city, value in cities.items():
    lst_xs.append(value[0])
    lst_ys.append(value[1])
solver = TSPSolver.from_data(lst_xs, lst_ys, norm="GEO")
solution = solver.solve()

# Extract the tour
tour = solution.tour
optimal_distance = solution.optimal_value

# Print the optimal route and distance
print("Optimal Route:", [list(cities.keys())[i] for i in tour])
print("Optimal Distance:", optimal_distance)

# Visualization code (optional)
coords = np.array([cities[city] for city in cities])
plt.figure(figsize=(10, 6))
plt.plot(coords[tour, 1], coords[tour, 0], marker='o')
for i, city in enumerate(cities):
    plt.text(coords[i, 1], coords[i, 0], city)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Optimal TSP Route")
plt.show()