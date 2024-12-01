# **Project Title:**
U-Value Calculation Tool for Windows and Glazing

# **Summary**
This Python-based tool calculates the U-Value of windows and glazing systems, simulating their impact on thermal insulation and daylight performance. It aids in optimizing energy efficiency in building design within BIM environments.

# **Role identification**
Our tool is specifically designed for the R2: OpenBIM Analyst role, with its primary objective being the analysis of standard IFC files to extract essential data related to windows and glazing materials. This data is presented in a comprehensive Excel sheet, providing valuable insights to aid sustainability engineers in their analysis and decision-making processes.


# **Focus Area and BIM Use**
Our project focuses on developing a tool that processes a standard IFC file to extract key information, such as the U-values of windows. The primary goal of this tool is to simplify the evaluation of window and glazing materials in a BIM model, providing sustainability engineers with all the essential data needed for their assessments. The tool is fully integrated within Blender, utilizing its scripting interface and the BlenderBIM add-on. The script has been written entirely in Python, ensuring seamless functionality and ease of use within the BIM workflow.


# **U-Value Calculation from IFC Files**

This repository contains a Python script that uses the **ifcopenshell** library to calculate the U-value of windows in an IFC model. The script automates the process of extracting material layer data from the IFC file and calculating the thermal transmittance (U-value) based on this information.

---

## **Use Case**

The script is designed for building designers and energy consultants who need to evaluate the thermal performance of windows within an IFC (Industry Foundation Classes) model. Specifically, the script calculates the U-value for each window element (`IfcPlate`) by analyzing its material layers' thickness and thermal conductivity.

---

## **How the Script Addresses the Problem**

Evaluating the U-value of windows is a critical step in assessing a building's energy efficiency. Manual calculation of U-values requires significant effort and expertise, as it involves extracting data from complex IFC files.

This script automates the process, providing a streamlined way to:
1. Extract material data for window layers directly from the IFC file.
2. Calculate the U-value based on the material properties.
3. Output the results for all windows in the IFC model.

This approach reduces human error, saves time, and ensures accurate U-value calculations.

---

## **For Users Without BIM Expertise**

This script is user-friendly and accessible to users with limited BIM knowledge. It handles the complexities of IFC schema internally, allowing users to:
- Run the script with minimal setup.
- Automatically extract material and thermal data for calculations.

All you need is:
1. An IFC file containing your building model.
2. Python installed on your system with the **ifcopenshell** library.

---

## **IFC Concepts**

The script leverages key concepts from Industry Foundation Classes (IFC), which is a standard for sharing Building Information Modeling (BIM) data. The following concepts are central to this script:

- **IFC File**: The input to the script is an IFC file, which encodes detailed information about a building's geometry, materials, and thermal properties.
- **Window Elements**: The script focuses on `IfcPlate` objects, commonly used to represent windows in the IFC schema.
- **Material Layer Data**: Each window's U-value is calculated using its associated material layers' thickness and thermal conductivity.

---

## **How the Script Works**

### **1. Loading the IFC Model**
The script begins by loading the IFC file using the **ifcopenshell** library. Replace the `ifc_file_path` variable with the path to your IFC file.

### **2. Extracting Material Layer Data**
For each window, the script extracts the following data:
- **Layer Thickness**: Converted from millimeters to meters.
- **Thermal Conductivity**: Retrieved from the material's properties.

### **3. Calculating the U-Value**
The U-value is calculated as the inverse of the total thermal resistance (\(R_{total}\)) of the window. Surface resistances are also considered during the calculation.

### **4. Outputting Results**
The script identifies all windows (`IfcPlate`) in the model and calculates their U-values. Results are printed to the console, showing each window's ID and U-value (or noting if the calculation is not possible).

---

## **Further Analysis**

This script provides a foundation for further BIM-based analysis. It can be extended to:
1. Evaluate energy performance for other building components, such as walls or roofs.
2. Perform daylight analysis or indoor climate simulations.
3. Check compliance with local energy codes, such as window-to-floor area ratios for balanced energy efficiency.

---

## **How to Run**

1. Install the required library:
   ```bash
   pip install ifcopenshell
