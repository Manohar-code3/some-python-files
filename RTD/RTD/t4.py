import numpy as np
import matplotlib.pyplot as plt

# Generate data points for the curve
x = np.linspace(-2, 2, 1000)
y = x**4 - x**2

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the curve
ax.plot(x, y, label='N-shaped Curve', color='blue')

# Add labels and a legend
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('N-shaped Curved Graph')
ax.legend()

# Display the graph
plt.show()
