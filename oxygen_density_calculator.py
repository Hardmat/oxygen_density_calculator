import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Constants
molar_mass_oxygen = 32  # g/mol
ideal_gas_constant = 0.0821  # atm * L / (mol * K)
molar_mass_oxygen_kg = molar_mass_oxygen / 1000  # kg/mol
molar_volume_conversion = 1000  # L/m^3

# Function to calculate density
def calculate_density(pressure, temperature):
    temperature_kelvin = temperature + 273.15  # Convert temperature to Kelvin
    pressure_atm = pressure / 14.6959488  # Convert pressure from PSI to atm
    density = (pressure_atm * molar_mass_oxygen_kg) / (ideal_gas_constant * temperature_kelvin)
    density = density * molar_volume_conversion  # Convert from g/L to kg/m^3
    return density

# Streamlit app
st.title("Gaseous Oxygen Density Calculator")

pressure = st.slider("Pressure (PSI)", 0, 200, step=1)
temperature = st.slider("Temperature (°C)", 0, 80, step=1)

density = calculate_density(pressure, temperature)
st.write("Density of gaseous oxygen:", density, "kg/m^3")

# Generate pressure and temperature values
pressure_values = np.linspace(0, 200, 100)
temperature_values = np.linspace(0, 80, 100)

# Calculate density for each pressure and temperature combination
density_values = np.zeros((100, 100))
for i, pressure_val in enumerate(pressure_values):
    for j, temperature_val in enumerate(temperature_values):
        density_values[i, j] = calculate_density(pressure_val, temperature_val)

# Create a meshgrid for the pressure and temperature values
pressure_grid, temperature_grid = np.meshgrid(pressure_values, temperature_values)

# Create a 3D plot of density
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(pressure_grid, temperature_grid, density_values, cmap="viridis")
ax.set_xlabel("Pressure (PSI)")
ax.set_ylabel("Temperature (°C)")
ax.set_zlabel("Density (kg/m^3)")
ax.set_title("Gaseous Oxygen Density")

# Add a red dot for the calculated density position
ax.scatter(pressure, temperature, density, color="red", s=50)

# Display the plot using st.pyplot
st.pyplot(fig)
