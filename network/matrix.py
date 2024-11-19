import os
import csv
import argparse

def process_latency_logs(log_dir):
    output_file_min = os.path.join(log_dir, "min_matrix.csv")
    output_file_avg = os.path.join(log_dir, "avg_matrix.csv")
    output_file_max = os.path.join(log_dir, "max_matrix.csv")

    # Initialize lists to hold the data for matrices
    nodes = []
    min_matrix = []
    avg_matrix = []
    max_matrix = []

    # Iterate through each log file in the directory
    for filename in sorted(
        [f for f in os.listdir(log_dir) if f.endswith(".log")],
        key=lambda x: int(x.split('-cpu')[1].split('.novalocal')[0])
    ):
        filepath = os.path.join(log_dir, filename)
        node_min = []
        node_avg = []
        node_max = []

        with open(filepath, 'r') as file:
            for line in file:
                if ':' in line:  # Ensure it's a valid fping line
                    parts = line.split(", min/avg/max = ")
                    if len(parts) == 2:
                        latency_stats = parts[1].strip().split("/")
                        if len(latency_stats) == 3:
                            node_min.append(float(latency_stats[0]))
                            node_avg.append(float(latency_stats[1]))
                            node_max.append(float(latency_stats[2]))

        # Add data for this node to the matrices
        nodes.append(filename.replace(".novalocal.log", "").replace("scc124-", ""))
        min_matrix.append(node_min)
        avg_matrix.append(node_avg)
        max_matrix.append(node_max)

    # Write the matrices to CSV files
    def save_to_csv(filename, matrix, nodes):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header row
            writer.writerow(["Node"] + nodes)
            # Write data rows
            for node, row in zip(nodes, matrix):
                writer.writerow([node] + row)

    save_to_csv(output_file_min, min_matrix, nodes)
    save_to_csv(output_file_avg, avg_matrix, nodes)
    save_to_csv(output_file_max, max_matrix, nodes)

    print(f"Latency matrices saved to CSV files: {output_file_min}, {output_file_avg}, {output_file_max}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process latency logs and generate CSV matrices.")
    parser.add_argument("log_dir", type=str, help="Path to the directory containing log files.")
    args = parser.parse_args()

    process_latency_logs(args.log_dir)

