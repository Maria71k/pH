def calculate_ph(hydrogen_ion_concentration):
    ph = -np.log10(hydrogen_ion_concentration)
    return ph

hydrogen_ion_concentration = 1e-7  # Example hydrogen ion concentration for neutral solution
ph = calculate_ph(hydrogen_ion_concentration)
print(f"pH: {ph}")
