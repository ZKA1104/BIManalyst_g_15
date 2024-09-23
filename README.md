# BIManalyst group 15
# Window Analysis Script using IFCOpenShell and BlenderBIM

## Use Case
The chosen use case is **Indoor and Energy** and **Daylight**. For these use cases, the script identifies the window height, width, area, and sill height for each window, along with a calculation of the total window area. The script is written in Python and is designed to be run in the Blender console where an IFC model is loaded using BlenderBIM.

## How the Script Addresses the Problem
1. **Loading the IFC Model:**  
   The IFC model is imported using `ifcopenshell`, which enables parsing and reading of the IFC file format. The BlenderBIM module, `IfcOpenShell.util.element`, is also imported to get additional properties, such as the sill height.

2. **Identifying Windows in the Model:**  
   The windows in the IFC model are identified by their object type, `IfcWindow`. The number of windows is determined by finding the length of the window list. For example, in the sample IFC file, there are 24 windows, numbered from 0 to 23.

3. **Extracting Window Properties:**  
   Using a loop, the script iterates through each identified window. For each window, it retrieves the height, width, and calculates the area (Area = height × width). Additional properties like the sill height are obtained using `ifcopenshell.util.element.get_psets(window)`. This information is printed out for each window, combining text with variables using string concatenation.

4. **Total Window Area Calculation:**  
   The script also sums the area of all windows and stores this in a variable that holds the total window area.

## Non-BIM Expertise
The mathematical formula used for area calculation is A = h × w. An Excel sheet containing all the window data from the IFC file is used to validate the correctness of the script's results. Daylight and Indoor Climate knowledge are applied to identify the relevant components for analysis.

## IFC Concepts
Before analyzing the use case, the architectural IFC model needs to be completed and loaded into BlenderBIM. The `IfcWindow` concept from the IFC schema is used to extract relevant attributes. From each `IfcWindow` object, the `Overall.Height` and `Overall.Width` attributes are extracted. Additional properties, such as the sill height, are obtained from `PSet_Revit_Constraints`. The window ID is used to link data to individual windows.

## Further Analysis
This script can be extended for broader analysis, such as energy consumption calculations, U-value assessments, or checks to ensure that the window-to-floor ratio exceeds 10%. It can also extract building elements like walls, floor areas, and lighting fixtures for further analysis. These studies are particularly relevant for Indoor Climate and Daylight engineers. Once the analysis for this use case is complete, the script can be adapted for other projects, such as Architectural or Installation projects.

## How to Run the Script
1. Install [BlenderBIM](https://blenderbim.org/).
2. Install the [IFCOpenShell library](https://github.com/IfcOpenShell/IfcOpenShell).
3. Load your IFC model into Blender.
4. Run the script in Blender’s Python console.

```python
import ifcopenshell
from rules import windowRule

model = ifcopenshell.open("path_to_your_ifc_file.ifc")
windowResult = windowRule.checkRule(model)

print("Window result:", windowResult)
