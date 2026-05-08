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

plt.plot(time, power, color = [0.8, 0.5, 0.9])
plt.xlabel("time $s$")
plt.ylabel("power $W$/$kg$")
plt.savefig("figures\power_curve.png")
plt.show()


