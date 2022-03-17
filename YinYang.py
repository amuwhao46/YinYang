import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""
By: Oke Amuwha
3/17/22
"""
theta = np.linspace(0, 2 * np.pi, 100)
radius = 4

#Coordinates for circle
x = radius * np.cos(theta)
y = radius * np.sin(theta)

#coordinates for sine wave
period = np.linspace(0, 2 * np.pi, 100)
y2 = np.sin(period)

#Plot and show data
plt.plot(period, y2)
plt.show()