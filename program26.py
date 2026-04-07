#name: harshvaya
#enrolment.no: 92400527205

'''Python program of Barplot with all parameters of a sample data   '''
import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]

plt.figure(figsize=(8,5))

plt.bar(
    categories, values,
    color='skyblue',
    edgecolor='black',
    linewidth=2,
    width=0.5,
    align='center',
    alpha=0.8,
    label='Values'
)

plt.title("Bar Plot Example", fontsize=16)
plt.xlabel("Categories", fontsize=12)
plt.ylabel("Values", fontsize=12)

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.show()