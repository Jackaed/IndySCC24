import subprocess
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import seaborn as sns
import pandas as pd


#node_nums = [1, 2, 3, 4]
#command = ["python", "ns_per_day.py", "-q", "-f", "file"]
#results = []
#
#for node_num in node_nums:
#    command[-1] = f"mpiapoa1-{node_num}-nodes.log"
#    result = subprocess.run(command, capture_output=True, text=True)
#
#    results.append(result.stdout)
#    results[-1] = float(results[-1][:-2])
#
#
node_nums = [1, 4, 8, 30]
results = [1370, 3651, 6651, 7029]
plt.scatter(node_nums, results)
# new_results = [0] + results
# new_node_nums = [0] + node_nums
# plt.plot(new_node_nums, new_results)
plt.xticks(range(1, 5))


m = np.sum(np.array(node_nums) * np.array(results)) / \
    np.sum(np.array(node_nums) ** 2)
# plt.plot(node_nums, [m * xi for xi in node_nums], color='red', label='Best Fit Line')

# Set the spines (axis lines) to intersect at (0, 0)
# plt.ylim(bottom=0)
# plt.xlim(0)

# Set bounds for the axes so they stop at the data range
# plt.gca().spines['bottom'].set_bounds(0, max(node_nums))
# plt.gca().spines['left'].set_bounds(0, max(results))

# m = np.sum(np.array(processor_nums) * np.array(results)) / np.sum(np.array(processor_nums) ** 2)
# plt.plot([0] + processor_nums, [0] + [m * xi for xi in processor_nums], color='red', label='Best Fit Line')

# Set the spines (axis lines) to intersect at (0, 0)
# plt.gca().spines['left'].set_position('zero')  # y-axis
# plt.gca().spines['bottom'].set_position('zero')  # x-axis

# Set bounds for the axes so they stop at the data range

plt.xlabel('Number of nodes')
plt.ylabel('Gflops')
plt.title('Performance vs number of nodes')

plt.savefig("hero_run_scaling.png")

plt.clf()

# time_to_core_ratio = [time/num_processor for time, num_processor
#                       in zip(results, processor_nums)]
#
# most_efficient = max(time_to_core_ratio)
#
# efficieny = [ratio / most_efficient for ratio in time_to_core_ratio]
#
# plt.scatter(processor_nums, efficieny)
#
# m, b = np.polyfit(processor_nums, efficieny, 1)
# plt.plot(processor_nums, [m * xi + b for xi in processor_nums], color='red', label='Best Fit Line')
#
# plt.ylim(0, 1.2)
#
# plt.xlabel('Number of processors')
# plt.ylabel('Efficiency')
#
# plt.title('Efficency for NAMD run on varying number of cores')
# plt.savefig("one_node_graph_efficiency.png")
