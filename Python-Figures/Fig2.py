import numpy as np
import matplotlib.pyplot as plt

size = 4
x = np.arange(size)
print(x)
Santa = [4,16,28,2]
Loreto = [3,15,26,3]
Guaymas = [4,13,19,4]

total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2
x1 = x + width
x2 = x + 2 * width
print(x)

string_x = ['2018', '2019', '2020', '2021']

plt.bar(x, Santa,  width=width, label='Santa Rosalia')
plt.bar(x1, Loreto, width=width, label='Loreto')
plt.bar(x2, Guaymas, width=width, label='Guaymas')
plt.xticks(x1, string_x)
for a, b in zip(x, Santa):
	plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=7)
for a, b in zip(x1, Loreto):
	plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=7)
for a, b in zip(x2, Guaymas):
	plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=7)
plt.ylabel("Number of times captured by Google Earth")
plt.legend()
plt.savefig("NumberOfTimesCapturedByGEP.pdf", format="pdf")
plt.show()
