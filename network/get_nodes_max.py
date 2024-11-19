import numpy as np
import itertools
import argparse

def find_best_n_nodes(matrix, num_nodes):
    n = matrix.shape[0]  # Total number of nodes
    min_max_delay = float('inf')
    best_combination = None

    # Iterate over all combinations of `num_nodes` nodes
    for nodes in itertools.combinations(range(n), num_nodes):
        submatrix = matrix[np.ix_(nodes, nodes)]

        # Calculate the max delay for the submatrix
        max_delay = np.max(submatrix)
  
        if max_delay < min_max_delay:
            min_max_delay = max_delay
            best_combination = nodes
    
    return best_combination, min_max_delay

def find_worst_n_nodes(matrix, num_nodes):
    n = matrix.shape[0]  # Total number of nodes
    max_max_delay = float('-inf')
    worst_combination = None

    # Iterate over all combinations of `num_nodes` nodes
    for nodes in itertools.combinations(range(n), num_nodes):
        submatrix = matrix[np.ix_(nodes, nodes)]

        # Calculate the max delay for the submatrix
        max_delay = np.max(submatrix)
  
        if max_delay > max_max_delay:
            max_max_delay = max_delay
            worst_combination = nodes
    
    return worst_combination, max_max_delay

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the best and worst n nodes based on latency.")
    parser.add_argument("csv_path", type=str, help="Path to the CSV file containing the delay matrix.")
    parser.add_argument("n", type=int, help="Number of nodes to analyze.")

    args = parser.parse_args()

    # Load the delay matrix from the CSV file
    delay_matrix = np.genfromtxt(args.csv_path, delimiter=',', skip_header=1)[:, 1:]

    best_nodes, best_delay = find_best_n_nodes(delay_matrix, args.n)
    worst_nodes, worst_delay = find_worst_n_nodes(delay_matrix, args.n)

    print(f"Best {args.n} nodes: {best_nodes}")
    print(f"Best delay: {best_delay}")
    print(f"Worst {args.n} nodes: {worst_nodes}")
    print(f"Worst delay: {worst_delay}")
