import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""
By: Oke Amuwha
3/17/22
"""
theta = np.linspace(0, 2 * np.pi, 100)
radius = 4

#Coordinates
x = radius * np.cos(theta)
y = radius * np.sin(theta)

#Equation


#Plot and show data
plt.plot(x,y)
plt.show()