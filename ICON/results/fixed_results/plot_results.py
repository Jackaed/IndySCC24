import subprocess
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# command = ["python", "ns_per_day.py", "-q", "-f", "file"]
# results = []
#
# for processor_num in processor_nums:
#     command[-1] = f"apoa1-{processor_num}.log"
#     result = subprocess.run(command, capture_output=True, text=True)
#
#     results.append(result.stdout)
#     results[-1] = float(results[-1][:-2])
init_performance = 3993.778
all_results = [[672.771, 368.784, 235.045],
           [358.975, 211.860, 126.142],
           [268.369, 148.050, 109.854],
           [201.624, 120.485, 81.913]]

# 1,1,
# 1,8,672.771
# 1,16,368.784
# 1,32,235.045
# 2,8,358.975
# 2,16,211.860
# 2,32,126.142
# 3,8,268.369
# 3,16,148.050
# 3,32,109.854
# 4,8,201.624
# 4,16,120.485
# 4,32,81.913



processor_nums = [8, 16, 32]
for i in range(len(all_results)):
    for j in range(len(all_results[i])):
        all_results[i][j] = init_performance/all_results[i][j]
        all_results[i][j] = all_results[i][j]/(processor_nums[j]*(i+1))

# Plotting with updated labels
plt.figure(figsize=(8, 6))
for idx, result in enumerate(all_results):
    plt.plot(processor_nums, result, label=f'Number of nodes: {idx + 1}')

plt.xlabel('Number of Processors')
plt.ylabel('Efficiency')
plt.title('Efficiency vs 1 Node 1 Core Run')
# plt.title('Time Taken on r02b04 vs Number of Processors')
plt.grid(True)
plt.legend()

plt.savefig("one_node_graph_efficiency.png")


# plt.clf()
#
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
# plt.title('Efficiency vs number of processors')
# plt.savefig("one_node_graph_efficiency.png")
