import matplotlib.pyplot as plt
import numpy as np

# Load the data
voltage = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
current = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])

# Plot the graph
plt.plot(voltage, current, 'bo-')

# Set the axis labels
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')

# Set the title
plt.title('I-V Curve of an InP-base Resonant Tunneling Diode')

# Show the plot
plt.show()
