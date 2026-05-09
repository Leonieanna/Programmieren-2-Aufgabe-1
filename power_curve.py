import numpy as np
import matplotlib.pyplot as plt
from sort import bubble_sort
from load_data import load_data

data = load_data('activity.csv')
power_W = data['PowerOriginal']
print(power_W)
sorted_power_W = bubble_sort(power_W)
print(sorted_power_W[::-1])
#nur wenn Datei direkt ausgeführt wird, nicht, wenn nur importiert wird. Das ist wichtig, damit die Funktion load_data auch von anderen Dateien importiert und verwendet werden kann, ohne dass der Code im if-Block automatisch ausgeführt wird.

# daten plotten
time = np.arange(1,1805)
power = sorted_power_W[::-1]

curve, = plt.plot(time, power, color = [0.7, 0.5, 0.95])
plt.title("power curve")
plt.xlabel("time [$s$]")
plt.ylabel("power [$W$/$kg$]")
plt.fill_between(time, power,
                 color=curve.get_color(),
                 alpha=0.3,
                 zorder=curve.get_zorder() - 1)
plt.margins(0,0)
plt.savefig("figures\power_curve.png")
plt.show()


