import matplotlib.pyplot as plt
import numpy as np

# Define the voltage range
voltage = np.linspace(0, 1, 100)  # Adjust the voltage range as needed

# Define the RTD characteristics
peak_current_density = 24.6  # kA/cm^2
valley_current_density = 2.86  # kA/cm^2

# Calculate the resistance for each voltage (you'll need actual resistance values)
resistance = np.where(voltage < 0.5, 1.0, 2.0)  # Placeholder values, adjust as needed

# Calculate the current using Ohm's law
current = voltage / resistance

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(voltage, current, label='Current vs Voltage', color='blue')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('RTD Characteristic: Current vs Voltage')
plt.grid(True)
plt.legend()
plt.show()
