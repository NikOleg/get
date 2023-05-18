from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker

with open("settings.txt", "r") as set:
    settings = [float(i) for i in set.read().split('\n')]

#Перевод показаний компаратора в вольты
data = numpy.loadtxt('data.txt', dtype = int) * (settings[1])

#Времена измерений
data_time = numpy.array([i*settings[0] for i in range(data.size)])

#Параметры фигуры
fig, ax = pyplot.subplots(figsize = (14, 8.5), dpi = 500)

#Минимальное и максимальное значение для осей
ax.axis([data.min(), data_time.max() + 1, data.min(), data.max() + 0.2])

#Интервалы основных делений
ax.xaxis.set_major_locator(ticker.MultipleLocator(4))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))

#Устанавливаем интервал вспомогательных делений
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

#Название графика с переноссом строки и центрированием
ax.set_title("\n".join(wrap('Процесс зарядки и разрядки конденсатора в RC-цепочке', 60)), loc = 'center')

#Основная и вторстепенная сетка
ax.grid(which = 'major', color = 'k')
ax.minorticks_on()
ax.grid(which = 'minor', color = 'gray', linestyle = ':')

#Подпись осей
ax.set_xlabel("Время, с")
ax.set_ylabel("Напряжение, В")

#Линия с легендой
ax.plot(data_time, data, c = 'black', linewidth = 1, label = 'U(t)')
ax.scatter(data_time[0:data.size:40], data[0:data.size:40], marker = 's', c = 'blue', s = 10)
ax.legend(shadow = False, loc = 'right', fontsize = 30)

#Время зарядки и разрядки
charge = data.argmax() * settings[0]
discharge = len(data) * settings[0] - charge
pyplot.text(6, 0.8, f'Время зарядки = {round(charge,2)}c')
pyplot.text(6, 0.9, f'Время разрядки = {round(discharge,2)}c')

#Сохранение
fig.savefig('graph.png')
fig.savefig('graph.svg')