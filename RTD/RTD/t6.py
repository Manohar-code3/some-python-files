import matplotlib.pyplot as plt
import numpy as np

# Set the peak current, peak voltage, valley current, and valley voltage
Ip = 10e-3
Vp = 0.5
Iv = 1e-3
Vv = 0.1

# Create a voltage array
V = np.linspace(0, Vp + Vv, 100)

# Calculate the current at each voltage
I = np.zeros_like(V)
for i in range(len(V)):
    if V[i] < Vp:
        I[i] = Ip
    elif V[i] < Vp + Vv:
        I[i] = Iv
    else:
        I[i] = 0

# Plot the I-V characteristics
plt.plot(V, I)

# Set the axis labels
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')

# Set the title
plt.title('I-V characteristics of a typical double barrier RTD')

# Show the plot
plt.show()
