import subprocess
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

processor_nums = [1, 2, 4, 8, 16]
command = ["python", "ns_per_day.py", "-q", "-f", "file"]
results = []

for processor_num in processor_nums:
    command[-1] = f"apoa1-{processor_num}.log"
    result = subprocess.run(command, capture_output=True, text=True)

    results.append(result.stdout)
    results[-1] = float(results[-1][:-2])

print(results)

plt.scatter(processor_nums, results)
m = np.sum(np.array(processor_nums) * np.array(results)) / np.sum(np.array(processor_nums) ** 2)
plt.plot([0] + processor_nums, [0] + [m * xi for xi in processor_nums], color='red', label='Best Fit Line')

# Set the spines (axis lines) to intersect at (0, 0)
plt.ylim(bottom=0)
plt.xlim(0)


plt.xlabel('Number of processors')
plt.ylabel('ns per day')
plt.title('Performance vs number of processors')

plt.savefig("one_node_graph_time.png")

plt.clf()

time_to_core_ratio = [time/num_processor for time, num_processor
                      in zip(results, processor_nums)]

most_efficient = max(time_to_core_ratio)

efficieny = [ratio / most_efficient for ratio in time_to_core_ratio]

plt.scatter(processor_nums, efficieny)

m, b = np.polyfit(processor_nums, efficieny, 1)
plt.plot(processor_nums, [m * xi + b for xi in processor_nums], color='red', label='Best Fit Line')

plt.ylim(0, 1.2)

plt.xlabel('Number of processors')
plt.ylabel('Efficiency')

plt.title('Efficiency vs number of processors')
plt.savefig("one_node_graph_efficiency.png")
