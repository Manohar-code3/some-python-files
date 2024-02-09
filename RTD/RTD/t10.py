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
]

spacer_layers = [
    (2e18, 160e-9),
    (2e16, 25e-9),
]

barrier_layers = [
    1.5e-9, 1.4e-9,
]

well_layers = [
    4.5e-9,
]

spacer_layers2 = [
    (2e16, 25e-9),
    (2e18, 25e-9),
]

emitter_layers = [
    (1e19, 200e-9),
]

substrate_thickness = 370e-6  # Semi-insulating InP substrate thickness

# Define the bias voltage range
voltage_range = np.linspace(-2.0, 2.0, 1000)

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

        tunneling_probability = 0.0
        for j in range(len(collector_layers)):
            Ec, Ev = collector_layers[j]
            Nc = 2 * (2 * np.pi * (m_eff * Ec) / (h_bar ** 2)) ** (3 / 2)
            Nv = 2 * (2 * np.pi * (m_eff * (Eg - Ev)) / (h_bar ** 2)) ** (3 / 2)
            tunneling_probability += Nc * Nv * np.exp(-integral_over_energy(Eg - Ec, Ec, V, m_eff, thickness)) * np.exp(-integral_over_energy(Ev, Eg - Ev, V, m_eff, thickness))

        I += e * A * tunneling_probability

    for i in range(len(spacer_layers)):
        n, thickness = spacer_layers[i]
        Ec = collector_layers[0][0]  # Conduction band energy from the previous layer
        Ev = -Ec  # Valence band energy

        # Calculate the energy levels for the spacer layer
        Ec -= e * V / thickness  # Electric field across the layer
        Ev -= e * V / thickness

        tunneling_probability = 0.0
        for j in range(len(spacer_layers)):
            Ec, Ev = spacer_layers[j]
            Nc = 2 * (2 * np.pi * (m_eff * Ec) / (h_bar ** 2)) ** (3 / 2)
            Nv = 2 * (2 * np.pi * (m_eff * (Eg - Ev)) / (h_bar ** 2)) ** (3 / 2)
            tunneling_probability += Nc * Nv * np.exp(-integral_over_energy(Eg - Ec, Ec, V, m_eff, thickness)) * np.exp(-integral_over_energy(Ev, Eg - Ev, V, m_eff, thickness))

        I += e * A * tunneling_probability

    for i in range(len(barrier_layers)):
        thickness = barrier_layers[i]
        Ec = spacer_layers[-1][0]  # Conduction band energy from the previous layer
        Ev = -Ec  # Valence band energy

        # Calculate the energy levels for the barrier layer
        Ec -= e * V / thickness  # Electric field across the layer
        Ev -= e * V / thickness

        tunneling_probability = 0.0
        for j in range(len(barrier_layers)):
            Ec, Ev = barrier_layers[j]
            Nc = 2 * (2 * np.pi * (m_eff * Ec) / (h_bar ** 2)) ** (3 / 2)
            Nv = 2 * (2 * np.pi * (m_eff * (Eg - Ev)) / (h_bar ** 2)) ** (3 / 2)
            tunneling_probability += Nc * Nv * np.exp(-integral_over_energy(Eg - Ec, Ec, V, m_eff, thickness)) * np.exp(-integral_over_energy(Ev, Eg - Ev, V, m_eff, thickness))

        I += e * A * tunneling_probability

    for i in range(len(well_layers)):
        thickness = well_layers
