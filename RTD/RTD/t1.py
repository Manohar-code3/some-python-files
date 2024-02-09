import numpy as np
import matplotlib.pyplot as plt

# Material properties data from Table I
voltage = np.linspace(-1.5, 1.5, 1000)  # Define a range of bias voltages

# Define properties for different materials
Si_properties = {
    "Electron mobility": 1500,
    "Relative dielectric constant": 11.9,
    "Energy bandgap": 1.12,
    "Electron effective mass": 0.98,
}
GaAs_properties = {
    "Electron mobility": 8500,
    "Relative dielectric constant": 13.1,
    "Energy bandgap": 1.424,
    "Electron effective mass": 0.063,
}
GaN_properties = {
    "Electron mobility": 400,
    "Relative dielectric constant": 10.4,
    "Energy bandgap": 3.44,
    "Electron effective mass": 0.27,
}

# Define a function to calculate current based on bias voltage and material properties
def current_voltage(voltage, properties):
    mobility = properties["Electron mobility"]
    dielectric_constant = properties["Relative dielectric constant"]
    bandgap = properties["Energy bandgap"]
    effective_mass = properties["Electron effective mass"]
    
    # Constants
    q = 1.60217663e-19  # Elementary charge in coulombs
    k = 1.380649e-23  # Boltzmann constant in joules per kelvin
    
    # Calculate current using the formula for RTD current
    current = (
        (q * mobility * dielectric_constant * bandgap ** 2) /
        (4 * k * effective_mass) *
        (np.exp((q * voltage) / (k * 300)) - 1) / 
        (1 + 2 * np.exp((-q * voltage) / (k * 300)))
    )
    return current

# Calculate current for different materials
Si_current = current_voltage(voltage, Si_properties)
GaAs_current = current_voltage(voltage, GaAs_properties)
GaN_current = current_voltage(voltage, GaN_properties)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(voltage, Si_current, label='Si')
plt.plot(voltage, GaAs_current, label='GaAs')
plt.plot(voltage, GaN_current, label='GaN')

plt.title('I-V Characteristics of a Double Barrier RTD')
plt.xlabel('Bias Voltage (V)')
plt.ylabel('Current (A)')
plt.legend()
plt.grid(True)
plt.show()
