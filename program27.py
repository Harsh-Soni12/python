#name: harshvaya
#enrolment.no: 92400527205

'''Python program of Pie-chart with all parameters of a sample data.    '''

import matplotlib.pyplot as plt

# Sample data
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [30, 25, 20, 25]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0.1, 0, 0, 0)  # explode first slice

plt.figure(figsize=(6,6))

plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    shadow=True,
    startangle=140,
    radius=1.2,
    wedgeprops={'edgecolor': 'black'},
    textprops={'fontsize': 12}
)

plt.title("Pie Chart Example", fontsize=16)
plt.legend(loc="upper right")

plt.show()