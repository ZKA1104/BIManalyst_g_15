import ifcopenshell

# Funktion til beregning af U-værdi
def calculate_u_value(layers):
    """
    Beregner U-værdien baseret på lagtykkelser og varmeledningsevne.
    
    layers: Liste af dictionaries med 'thickness' (i meter) og 'conductivity' (W/mK)
    """
    R_total = 0

    # Indvendig og udvendig varmeovergangsmodstand (standardværdier)
    Rsi = 0.13  # m²·K/W
    Rse = 0.04  # m²·K/W
    Rsl = 1.753 # m²·K/W
    
    # Start med overgangsmodstandene
    R_total += Rsi + Rse + Rsl

    # Tilføj modstand for hvert lag
    for layer in layers:
        thickness = layer.get("thickness", 0)
        conductivity = layer.get("conductivity", 0)
        if thickness > 0 and conductivity > 0:
            R_total += thickness / conductivity

    # Beregn U-værdi
    if R_total > 0:
        return 1 / R_total
    else:
        return None  # Returnér None, hvis beregning ikke er mulig

# Funktion til at hente materialelag for et vindue fra en IFC-fil
def get_window_layers(IfcPlate):
    """
    Henter materialelag for et givet vindue fra IFC-filen.
    
    window: IfcWindow-objekt
    Returnerer en liste af lag med tykkelse og varmeledningsevne.
    """
    layers = []
    
    # Find materialer knyttet til vinduet
    if hasattr(IfcPlate, "IsDefinedBy"):
        for definition in IfcPlate.IsDefinedBy:
            if definition.is_a("IfcRelAssociatesMaterial"):
                material = definition.RelatingMaterial
                if material.is_a("IfcMaterialLayerSet"):
                    for layer in material.MaterialLayers:
                        thickness = getattr(layer, "LayerThickness", 0) / 100  # Omregn til meter
                        conductivity = getattr(layer.Material, "ThermalConductivity", None)
                        layers.append({"thickness": thickness, "conductivity": conductivity})
    
    return layers

# Åbn IFC-modellen
ifc_file_path = "C:\\Users\\mikae\\OneDrive\\Dokumenter\\DTU BYGNINGSDESIGN\\3.semster\\41934 Advanced Building Information Modeling\\CES_BLD_24_06_ARC.IFC"
model = ifcopenshell.open(ifc_file_path)

# Find alle vinduer i modellen
windows = model.by_type("IfcPlate")

# Beregn og print U-værdier for vinduer
for window in windows:
    layers = get_window_layers(window)
    u_value = calculate_u_value(layers)
    if u_value:
        print(f"Window ID: {window.GlobalId}, U-value: {u_value:.3f} W/m²K")
    else:
        print(f"Window ID: {window.GlobalId}, U-value could not be calculated")