#name: harshvaya
#enrolment.no: 92400527205

'''Python program of Line plot with all parameters of a sample data.    '''

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.figure(figsize=(8,5))

plt.plot(
    x, y,
    color='blue',
    linestyle='--',
    linewidth=2,
    marker='o',
    markersize=8,
    markerfacecolor='red',
    markeredgecolor='black',
    alpha=0.9,
    label='Line Data'
)

plt.title("Line Plot Example", fontsize=16)
plt.xlabel("X-axis", fontsize=12)
plt.ylabel("Y-axis", fontsize=12)

plt.grid(True)
plt.legend()

plt.show()