from matplotlib.pyplot import figure
from numpy import arange

x = arange(1, 11, 1)
y = x ** 2
x_labels = list('abcdefghij')
x_ticks = range(len(x_labels))
figura = figure(figsize=(15, 11.25), dpi=90)
subplot = figura.add_subplot(1, 1, 1)
subplot.plot(y)
subplot.set_xticks(x_ticks)
subplot.set_xticklabels(x_labels)
figura.savefig('grafico.png')
