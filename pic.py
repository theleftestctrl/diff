import matplotlib.pyplot as plt
from sys import argv
import numpy as np
import numpy as np

def load_data_from_folder(folder):
    def load(name):
        data = []
        with open(f'{folder}/{name}') as f:
            for line in f:
                data.append([float(x.replace(',', '.')) for x in line.split()])
        return np.array(data)
    return load


file_name = argv[1]
load_data = load_data_from_folder('.')
data = load_data(file_name)

x = data[:, 0]
y = data[:, 1]
ydif = data[:, 2]

fig, ax = plt.subplots()        # Создание поля для рисунка (fig) и осей (ax)

ax.plot(x, y, color='C0', marker='', linestyle='-', label=r'$ax^2+bx+c$')
ax.plot(x, ydif, color='C1', marker='', linestyle='-', label=r'$(ax^2+bx+c)`$')

ax.legend(loc="best", labelcolor='markeredgecolor')

fig.savefig('picture.pdf')
