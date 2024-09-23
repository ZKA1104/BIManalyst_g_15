import ifcopenshell


from rules import windowRule

model = ifcopenshell.open("C:\\Users\\mikae\\OneDrive\\Dokumenter\\DTU BYGNINGSDESIGN\\3.semster\\41934 Advanced Building Information Modeling\\CES_BLD_24_06_ARC.IFC")

windowResult = windowRule.checkRule(model)

print("Window result:", windowResult)





