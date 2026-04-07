#name:harshvaya
#enrolment.no:92400527205


'''Python program of Box Plot with all parameters of a sample data. '''

import matplotlib.pyplot as plt

# Sample data
data = [
    [10, 20, 30, 40, 50],
    [15, 25, 35, 45, 55],
    [5, 10, 15, 20, 25]
]

plt.figure(figsize=(8,5))

plt.boxplot(
    data,
    notch=True,
    patch_artist=True,
    widths=0.6,
    vert=True,
    showmeans=True,
    meanline=True,
    labels=['A', 'B', 'C'],
    boxprops=dict(facecolor='lightblue', color='black'),
    whiskerprops=dict(color='black'),
    capprops=dict(color='black'),
    medianprops=dict(color='red'),
    flierprops=dict(marker='o', color='green', alpha=0.5)
)

plt.title("Box Plot Example", fontsize=16)
plt.xlabel("Groups")
plt.ylabel("Values")

plt.grid(True)
plt.show()