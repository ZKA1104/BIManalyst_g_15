import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()
things = file.by_type('IfcPlate')
print(len(things))
