import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# make data

x_points_serious_a = np.arange(0, 1000000, 100000)
y_points_serious_a = np.random.rand(10) * 10

x_points_serious_b = np.arange(0, 1000000, 100000)
y_points_serious_b = np.random.rand(10) * 10

plt.plot(x_points_serious_b, y_points_serious_b, label="line2")
plt.plot(x_points_serious_a, y_points_serious_a, label="line1")
# draw points with holo circles
plt.scatter(x_points_serious_a, y_points_serious_a, s=60, facecolors='none', edgecolors='r')
plt.scatter(x_points_serious_b, y_points_serious_b, s=60, facecolors='none', edgecolors='r')

# Create a ScalarFormatter for the x-axis
formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1, 1))  # Adjust the power limits as needed
plt.gca().xaxis.set_major_formatter(formatter)

plt.xlabel("this is x label")
plt.ylabel("this is y label")
plt.title("this is title")
plt.legend()
plt.show()
