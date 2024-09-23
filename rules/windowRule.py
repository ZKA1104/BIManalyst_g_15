import ifcopenshell

def checkRule(model):
    windows = model.by_type('IfcPlate')

    result = f"There are: {len(windows)} windows."

    return result

