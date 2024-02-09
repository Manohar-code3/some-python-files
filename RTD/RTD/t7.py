import numpy as np
import matplotlib.pyplot as plt

# Constants and parameters (These are tailored to create a mirrored N-shaped curve)
V_min = -0.2  # Minimum voltage
V_max = 0.2  # Maximum voltage
num_points = 1000  # Number of data points

# Define voltage range
voltage = np.linspace(V_min, V_max, num_points)

# RTD I-V characteristics (Mirrored N-shaped curve)
def rtd_iv(voltage):
    # Define RTD parameters for a mirrored N-shaped curve
    V_peak1 = -0.05  # First peak voltage
    I_peak1 = 0.002  # First peak current
    V_peak2 = 0.05   # Second peak voltage
    I_peak2 = 0.002  # Second peak current

    # Current-voltage relationship for a mirrored N-shaped RTD
    I = np.piecewise(voltage, [voltage < -V_peak2, (-V_peak2 <= voltage) & (voltage < -V_peak1), (V_peak1 <= voltage) & (voltage < V_peak2), voltage >= V_peak2],
                    [0,
                     lambda x: I_peak2 * (1 - np.exp(-0.1 * (x + V_peak2)**2)),
                     lambda x: I_peak1 * (1 - np.exp(-0.1 * (x + V_peak1)**2)),
                     0])

    return I

current = rtd_iv(voltage)

# Create the mirrored N-shaped I-V curve plot
plt.figure()
plt.plot(voltage, current, label="I-V Curve")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.title("Double-Barrier Resonant Tunneling Diode (RTD) I-V Curve (InP)")
plt.grid(True)
plt.legend()
plt.show()
