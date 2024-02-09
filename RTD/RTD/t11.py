import numpy as np
import matplotlib.pyplot as plt

# Constants
e = 1.602176634e-19  # Elementary charge in C
kB = 8.617333262145e-5  # Boltzmann constant in eV/K
T = 300  # Temperature in K
Eg = 0.75  # Energy bandgap of InP in eV
h_bar = 1.0545718e-34  # Reduced Planck's constant in J·s
A = 1e-12  # Device cross-sectional area in m^2
m_eff = 0.08 * 9.10938356e-31  # Effective electron mass in kg

# Define the tunneling probability function
def calculate_tunneling_probability(energy, V, m_eff, width):
    k = np.sqrt(2 * m_eff * (V - energy)) / h_bar
    tunneling_probability = np.exp(-2 * k * width)
    return tunneling_probability

# Define the function to calculate the integral over energy
def integral_over_energy(E1, E2, V, m_eff, width):
    E_lower = min(E1, E2)
    E_upper = max(E1, E2)
    
    num_points = 1000  # Number of integration points (adjust as needed)
    delta_E = (E_upper - E_lower) / num_points
    integral = 0.0

    for i in range(num_points):
        energy = E_lower + i * delta_E
        tunneling_probability = calculate_tunneling_probability(energy, V, m_eff, width)
        integral += tunneling_probability

    return integral * delta_E

# Provided parameters
collector_layers = [
    (3e19, 40e-9),
    (2e18, 160e-9),                                                                        
    (2e16, 25e-9)
]

# Define the bias voltage range
voltage_range = np.linspace(0, 1, 10)

# Initialize arrays to store current and voltage values
current_values = []

# Calculate current for each bias voltage
for V in voltage_range:
    I = 0.0

    for i in range(len(collector_layers)):
        n, thickness = collector_layers[i]
        Ec = 0.0  # Conduction band energy
        Ev = -Ec  # Valence band energy

        # Calculate the energy levels for the collector layer
        Ec -= e * V / thickness  # Electric field across the layer
        Ev -= e * V / thickness

        # Check if the energy levels result in a negative square root
        if V - Ec >= 0:
            k = np.sqrt(2 * m_eff * (V - Ec)) / h_bar
        else:
            k = 0.0  # Handle the invalid case

        # Calculate Nc only if k is valid
        if k > 0:
            Nc = 2 * (2 * np.pi * (m_eff * Ec) / (h_bar ** 2)) ** (3 / 2)
        else:
            Nc = 0.0  # Handle the invalid case

        # Continue with the rest of your calculations
        # ...

        tunneling_probability = 0.0
        for j in range(len(collector_layers)):
            # Check if Nc is valid
            if Nc > 0:
                Ec, Ev = energy_levels[j]
                Nv = 2 * (2 * np.pi * (m_eff * (Eg - Ev)) / (h_bar ** 2)) ** (3 / 2)
                tunneling_probability += Nc * Nv * np.exp(-integral_over_energy(Eg - Ec, Ec, V, m_eff, thickness)) * np.exp(-integral_over_energy(Ev, Eg - Ev, V, m_eff, thickness))

        I += e * A * tunneling_probability
    
    current_values.append(I)

# Plot the I-V curve
plt.figure()
plt.plot(voltage_range, current_values, label="I-V Curve")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.title("InP Resonant Tunneling Diode I-V Characteristic")
plt.grid()
plt.legend()
plt.show()

