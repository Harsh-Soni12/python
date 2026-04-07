#name:harshvaya
#enrolment.no:92400527205


'''Python program of Scatter Plot with all parameters of a sample 
data.  '''

import matplotlib.pyplot as plt

# Sample data
x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

sizes = [20, 50, 100, 200, 80, 60, 120, 90]
colors = [10, 20, 30, 40, 50, 60, 70, 80]

plt.figure(figsize=(8,5))

plt.scatter(
    x, y,
    s=sizes,
    c=colors,
    cmap='viridis',
    alpha=0.8,
    edgecolors='black',
    linewidth=1,
    marker='o',
    label='Data Points'
)

plt.title("Scatter Plot Example", fontsize=16)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.colorbar()
plt.legend()
plt.grid(True)

plt.show()