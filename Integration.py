import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


# Defining function
def function(x):
    return np.abs(x)


fig, ax = plt.subplots()

# Limits of Integration
x_0 = -2  # lower limit
x_n = 3  # upper limit

# Step
step = 0.0001
step_in = step + x_0

suma = []

while step_in <= x_n:
    y = function(step_in)
    suma.append(y * step)
    step_in += step
    ax.add_patch(Rectangle((step_in - step, 0), step, y, edgecolor="#6699FF", fill="#99CCFF"))

if x_0 < 0:
    xx = x_0 + x_0 / 2
else:
    xx = x_0 - x_0 / 2

if x_n < 0:
    yy = x_n - x_n / 2
else:
    yy = x_n + x_n / 2

x_lim = np.linspace(xx, yy, 100000)

ax.plot(x_lim, function(x_lim), color="red")
ax.plot([xx, yy], [0, 0], color="black", linewidth=0.8)

plt.title(f"Pole od {round(x_0, 3)} do {round(x_n, 3)} wynosi {round(sum(suma), 3)}")
plt.xlim([xx, yy])
plt.show()
