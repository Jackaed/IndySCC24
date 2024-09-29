import subprocess
import numpy as np
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
print(len(results))

plt.scatter(processor_nums, results)
m, b = np.polyfit(processor_nums, results, 1)
plt.plot(processor_nums, [m * xi + b for xi in processor_nums], color='red', label='Best Fit Line')

plt.xlabel('Number of processors')
plt.ylabel('Time')
plt.title('NAMD run on varying number of processors')

plt.savefig("one_node_graph.png")

plt.show()
