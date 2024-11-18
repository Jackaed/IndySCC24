import matplotlib.pyplot as plt

# Data
node_nums = [0, 1, 4, 8, 30]
results = [0, 1370, 3651, 6651, 7029]

# Plotting the graph with adjusted axis limits
plt.figure(figsize=(8, 6))
plt.plot(node_nums, results, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
plt.xlabel('Number of Nodes')
plt.ylabel('Performance (Gflops)')
plt.title('HPL Performance Scaling with Number of Nodes')
plt.ylim(0, max(results) * 1.1)  # Setting y-axis to start at 0 and adding padding above
plt.xlim(0, max(node_nums))  # Removing padding on x-axis to start line in the bottom-left corner
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('hero_run_node_scaling.png', dpi=300)
plt.show()

