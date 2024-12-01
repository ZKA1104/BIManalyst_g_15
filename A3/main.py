import ifcopenshell

# Here the function for calculating the U-value is being defined
def calculate_u_value(layers):
    """
    Beregner U-værdien baseret på lagtykkelser og varmeledningsevne.
    
    layers: Liste af dictionaries med 'thickness' (i meter) og 'conductivity' (W/mK)
    """
    R_total = 0

    # The interior and exterior heat transfer default value is being defined.
    Rsi = 0.13  # m²·K/W
    Rse = 0.04  # m²·K/W
    Rsl = 1.753 # m²·K/W
    
    # The sum of the heat transfer value is calculated
    R_total += Rsi + Rse + Rsl

    # A resistance for each of the layers is being added to the heat transfer value
    for layer in layers:
        thickness = layer.get("thickness", 0)
        conductivity = layer.get("conductivity", 0)
        if thickness > 0 and conductivity > 0:
            R_total += thickness / conductivity

    # The U-value is calculated by using the formula
    if R_total > 0:
        return 1 / R_total
    else:
        return None  # Returnér None, hvis beregning ikke er mulig

# This function draws out the material from the IFC-file, if the material is available.
def get_window_layers(IfcPlate):
    """
Gets material layers for a given window from the IFC file.
    
    window: IfcWindow-objekt
    Returns a list of layers with thickness and thermal conductivity.

    """
    layers = []
    
# Find materials attached to the window
    if hasattr(IfcPlate, "IsDefinedBy"):
        for definition in IfcPlate.IsDefinedBy:
            if definition.is_a("IfcRelAssociatesMaterial"):
                material = definition.RelatingMaterial
                if material.is_a("IfcMaterialLayerSet"):
                    for layer in material.MaterialLayers:
                        thickness = getattr(layer, "LayerThickness", 0) / 100  # Convert to meter
                        conductivity = getattr(layer.Material, "ThermalConductivity", None)
                        layers.append({"thickness": thickness, "conductivity": conductivity})
    
    return layers

# Open the IFC-model   
ifc_file_path = "C:\\Users\\mikae\\OneDrive\\Dokumenter\\DTU BYGNINGSDESIGN\\3.semster\\41934 Advanced Building Information Modeling\\CES_BLD_24_06_ARC.IFC"
model = ifcopenshell.open(ifc_file_path)

# Find all windows in the model
windows = model.by_type("IfcPlate")

# Calculate the U-value and print output
for window in windows:
    layers = get_window_layers(window)
    u_value = calculate_u_value(layers)
    if u_value:
        print(f"Window ID: {window.GlobalId}, U-value: {u_value:.3f} W/m²K")
    else:
        print(f"Window ID: {window.GlobalId}, U-value could not be calculated")
