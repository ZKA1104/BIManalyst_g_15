import ifcopenshell

from rules import windowRule
from rules import doorRule

model = ifcopenshell.open("path/to/ifcfile.ifc")

windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)

import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()
things = file.by_type('IfcPlate')
print(len(things))


