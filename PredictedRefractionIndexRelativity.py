import numpy as np

# Speed of light in vacuum
c = 299792458  # m/s

# Wavelength range from 380 nm to 700 nm (visible spectrum)
wavelengths = np.array([100, 200, 300, 380, 460, 540, 620, 700, 1000, 2000, 5000])  # nm


# Incident angle (in radians)
theta1 = np.radians(3)  # 45 degrees incidence angle

# Materials properties
materials_properties = {
    "barium titanate": {"permittivity": 2300.0, "permeability": 1.0},
    "water": {"permittivity": 80.1, "permeability": 0.999992},
    "lithium niobate": {"permittivity": 28.0, "permeability": 1.0},
    "silicon": {"permittivity": 11.9, "permeability": 1.0},
    "germanium": {"permittivity": 16.0, "permeability": 1.0},
    "gallium arsenide": {"permittivity": 13.1, "permeability": 1.0},
    "crown glass": {"permittivity": 7.0, "permeability": 1.0},
    "flint glass": {"permittivity": 7.4, "permeability": 1.0},
    "diamond": {"permittivity": 5.7, "permeability": 0.999992},
    "fused silica": {"permittivity": 3.82, "permeability": 1.0},
    "Acrylic (PMMA)": {"permittivity": 3.0, "permeability": 1.0},
    "Polycarbonate": {"permittivity": 2.95, "permeability": 1.0},
    "Sapphire (Al2O3)": {"permittivity": 9.4, "permeability": 1.0},
}

# Empirical refractive indices
materials_refractive_index = {
    "water": [ 1,1, 1, 1.3330, 1.3300, 1.3260, 1.3230, 1.3200, 1, 1, 1 ],
    "crown glass": [ 1, 1, 1, 1.5230, 1.5180, 1.5120, 1.5070, 1.5020, 1, 1, 1],
    "flint glass": [ 1, 1, 1,1.6200, 1.6120, 1.6030, 1.5960, 1.5880, 1, 1,1 ],
    "diamond": [ 1, 1, 1, 2.4190, 2.4020, 2.3840, 2.3690, 2.3540, 1,1,1 ],
    "silicon": [ 1,1,1, 3.9760, 3.9690, 3.9590, 3.9520, 3.9440,1,1,1  ],
    "germanium": [ 1, 1, 1, 4.0520, 4.0370, 4.0200, 4.0070, 3.9940, 1,1,1 ],
    "gallium arsenide": [ 1, 1, 1, 3.8850, 3.8740, 3.8610, 3.8500, 3.8390, 1, 1, 1 ],
    "fused silica": [ 1, 1, 1, 1.4580, 1.4570, 1.4550, 1.4540, 1.4530, 1, 1, 1 ],
    "barium titanate": [ 1, 1, 1, 2.4130, 2.4060, 2.3970, 2.3910, 2.3840, 1,1,1 ],
    "lithium niobate": [ 1, 1, 1, 2.2360, 2.2290, 2.2190, 2.2130, 2.2060, 1,1,1 ],
    "Acrylic (PMMA)":   [ 1, 1, 1, 1.508, 1.496, 1.491, 1.488, 1.486, 1, 1, 1 ],
    "Polycarbonate":    [ 1, 1, 1, 1.62, 1.596, 1.584, 1.577, 1.573, 1, 1, 1 ],
    "Sapphire (Al2O3)": [ 1, 1, 1, 1.788, 1.775, 1.769, 1.764, 1.760, 1, 1, 1 ],
}


# Scaling factors for each material
scaling_factors = {
    "water": 0.1476,
    "crown glass": 0.5694,
    "flint glass": 0.5871,
    "diamond": 0.9949,
    "silicon": 1.1435,
    "germanium": 1.0013,
    "gallium arsenide": 1.0629,
    "fused silica": 0.7417,
    "barium titanate": 0.0498,
    "lithium niobate": 0.4178,
    "Acrylic (PMMA)": 0.8577,
    "Polycarbonate": 0.9189,
    "Sapphire (Al2O3)": 0.5749,
}

def speed_of_light_in_material(permittivity_r, permeability_r):
    return c / np.sqrt(permittivity_r * permeability_r)

def refractive_index(c, v_material):
    return c / v_material

def snell_law(n1, n2, theta1):
    return np.arcsin((n1 / n2) * np.sin(theta1))

def adjust_for_frequency(n_predicted, wavelength):
    # Constants
    c = 299792458  # Speed of light in m/s
    h = 6.62607015e-34  # Planck's constant in J⋅s
    
    # Calculate frequency and photon energy
    frequency = c / (wavelength * 1e-9)  # Convert wavelength to meters
    photon_energy = h * frequency
    
    # Adjust parameters for energy scaling - optimized values
    alpha = 1.0000000000e-16  # Scaling factor
    beta = 2.9281     # Power factor for energy dependence
    
    # Nonlinear energy-dependent scaling factor
    energy_factor = 1 + alpha * (photon_energy ** beta)
    
    # Adjust wavelength scaling: Using a quadratic term for better fit
    wavelength_offset = 758.0  # Central wavelength for adjustment
    wavelength_factor = 1 + 5.8567014699e-05 * ((wavelength_offset - wavelength) ** 2) / wavelength_offset
    
    lowend = 218.2
    if (wavelength < lowend):
        return n_predicted * wavelength_factor * energy_factor - (wavelength_factor * 0.0188) * abs(lowend/wavelength)
   
    highend = 648.4
    if (wavelength > highend):
        return n_predicted * wavelength_factor * energy_factor - (wavelength_factor * 0.0100) * abs(highend/wavelength)
   
    # Apply both energy and wavelength scaling
    return n_predicted * wavelength_factor * energy_factor

def calculate_percent_difference(observed, predicted):
    return abs(observed - predicted) / max(observed, predicted)* 100

def main():

    count = 0
    total_error = 0

    print(f"Wavelength:  nm")
    print(f"  Empirical Refractive Index (n2): ")
    print(f"  Predicted Refractive Index (n_pre): ")
    print(f"  Refractive Index % Difference: %")
    print(f"  Snell's Law Angle (empirical): degrees")
    print(f"  Snell's Law Angle (predicted): degrees")
    print(f"  Angle % Difference: %")
    print("-" * 50)
    print(" " * 50)
    for material, refractive_indices in materials_refractive_index.items():
        print(f"\nMaterial: {material}")
        
        permittivity_r = materials_properties[material]["permittivity"]
        permeability_r = materials_properties[material]["permeability"]
        
        v_material = speed_of_light_in_material(permittivity_r, permeability_r)
        n_predicted_base = refractive_index(c, v_material)
        
        for n2_empirical, wavelength in zip(refractive_indices, wavelengths):
            if n2_empirical==1 : continue
            n_predicted = adjust_for_frequency(n_predicted_base, wavelength)
            
            # Apply the scaling factor
            n_predicted_scaled = n_predicted * scaling_factors[material] 
            
            theta2_empirical = snell_law(1.0003, n2_empirical, theta1)
            theta2_empirical_deg = np.degrees(theta2_empirical)
            
            theta2_predicted = snell_law(1.0003, n_predicted_scaled, theta1)
            theta2_predicted_deg = np.degrees(theta2_predicted) 
            
            # Calculate percentage differences
            n_percent_diff = calculate_percent_difference(n2_empirical, n_predicted_scaled)
            angle_percent_diff = calculate_percent_difference(theta2_empirical_deg, theta2_predicted_deg)

            total_error += angle_percent_diff
            count += 1
            
            print(f"{wavelength:<4} nm {n2_empirical:.4f} {n_predicted_scaled:.4f} {n_percent_diff:.4f}% {theta2_empirical_deg:.4f} {theta2_predicted_deg:.4f} {angle_percent_diff:.4f}%")

    print()
    print(f"Average Error: {total_error/count:.4f}%")
    print()

def main_():
    # Initialize the scaling factors dictionary
    scaling_factors = {}

    # Center wavelength for scaling calculation
    center_wavelength = 540

    for material, refractive_indices in materials_refractive_index.items():
        # Get material properties
        permittivity_r = materials_properties[material]["permittivity"]
        permeability_r = materials_properties[material]["permeability"]
        
        # Calculate the predicted base refractive index without adjustments
        v_material = speed_of_light_in_material(permittivity_r, permeability_r)
        n_predicted_base = refractive_index(c, v_material)
        
        # Find the empirical refractive index for the center wavelength
#        center_index = wavelengths.index(center_wavelength)
        #n2_empirical_center = refractive_indices[center_index]
        n2_empirical_center = refractive_indices[5]
        
        # Adjust the predicted refractive index for the center wavelength
        n_predicted_center = adjust_for_frequency(n_predicted_base, center_wavelength)
        
        # Calculate the scaling factor (ratio between predicted and empirical)
        scaling_factor = n2_empirical_center / n_predicted_center
        
        # Store the scaling factor in the dictionary
        scaling_factors[material] = scaling_factor

    # Print scaling factors in the required format
    print("\n# Scaling factors for each material")
    print("scaling_factors = {")
    for material, factor in scaling_factors.items():
        print(f'    "{material}": {factor:.4f},')
    print("}")
if __name__ == "__main__":
    main()
