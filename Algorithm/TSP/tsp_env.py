from concorde.tsp import TSPSolver
from concorde.tests.data_utils import get_dataset_path


fname = get_dataset_path("berlin52")
solver = TSPSolver.from_tspfile(fname)
solution = solver.solve()
if solution.found_tour:
    print("Optimal tour found")
    print(solution.optimal_value)
    print(solution.tour)
