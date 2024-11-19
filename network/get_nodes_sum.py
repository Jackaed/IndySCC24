import numpy as np
import itertools
import argparse

def find_best_n_nodes(matrix, num_nodes):
    n = matrix.shape[0]  # Total number of nodes
    min_total_delay = float('inf')
    best_combination = None

    # Iterate over all combinations of `num_nodes` nodes
    for nodes in itertools.combinations(range(n), num_nodes):
        submatrix = matrix[np.ix_(nodes, nodes)]

        # Calculate the total delay for the submatrix, excluding diagonal elements
        total_delay = np.sum(submatrix) - np.sum(np.diagonal(submatrix))
  
        if total_delay < min_total_delay:
            min_total_delay = total_delay
            best_combination = nodes

    # Calculate the average delay for the best combination
    avg_delay = min_total_delay / max(1, (num_nodes * (num_nodes - 1) / 2))  # Unique pairs
    return best_combination, avg_delay

def find_worst_n_nodes(matrix, num_nodes):
    n = matrix.shape[0]  # Total number of nodes
    max_total_delay = float('-inf')
    worst_combination = None

    # Iterate over all combinations of `num_nodes` nodes
    for nodes in itertools.combinations(range(n), num_nodes):
        submatrix = matrix[np.ix_(nodes, nodes)]

        # Calculate the total delay for the submatrix, excluding diagonal elements
        total_delay = np.sum(submatrix) - np.sum(np.diagonal(submatrix))

        if total_delay > max_total_delay:
            max_total_delay = total_delay
            worst_combination = nodes

    # Calculate the average delay for the worst combination
    avg_delay = max_total_delay / max(1, (num_nodes * (num_nodes - 1) / 2))  # Unique pairs
    return worst_combination, avg_delay

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the best and worst n nodes based on latency.")
    parser.add_argument("csv_path", type=str, help="Path to the CSV file containing the delay matrix.")
    parser.add_argument("n", type=int, help="Number of nodes to analyze.")

    args = parser.parse_args()

    # Load the delay matrix from the CSV file
    delay_matrix = np.genfromtxt(args.csv_path, delimiter=',', skip_header=1)[:, 1:]

    best_nodes, best_avg_delay = find_best_n_nodes(delay_matrix, args.n)
    worst_nodes, worst_avg_delay = find_worst_n_nodes(delay_matrix, args.n)

    print(f"Best {args.n} nodes: {best_nodes}")
    print(f"Best average delay: {best_avg_delay}")
    print(f"Worst {args.n} nodes: {worst_nodes}")
    print(f"Worst average delay: {worst_avg_delay}")

