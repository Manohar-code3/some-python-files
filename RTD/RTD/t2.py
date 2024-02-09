import matplotlib.pyplot as plt
import numpy as np

# Define the parameters of the RTD.
V = np.linspace(-1.5, 1.5, 1000)  # Voltage (V)
I = np.zeros(len(V))  # Current (A)

# Calculate the current through the RTD using the following equation:
# I = J * A
# where:
# J is the current density (A/cm²)
# A is the area of the RTD (cm²)

cond = V < -0.5
boolean_array = np.where(cond, 0, 1)

J = np.piecewise(
    boolean_array,
    [boolean_array, ~boolean_array],
    [
        lambda V: 0,
        lambda V: 1e6 * (V + 0.5) ** 2,
    ],
)

A = 1e-6  # Area of the RTD (cm²)

I = J * A

# Plot the I-V curve of the RTD.
plt.plot(V, I)

# Label the axes.
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")

# Title the plot.
plt.title("I-V Curve of InP RTD")

# Display the plot.
plt.show()
