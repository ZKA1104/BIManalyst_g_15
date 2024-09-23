# BIManalyst group 15
# IFC Model Rule Checking Script

This repository contains a Python script that uses the **ifcopenshell** library to analyze an IFC model file and apply specific rules related to building components—in this case, windows—via a custom `windowRule`.

## Use Case

The script is designed to check an IFC (Industry Foundation Classes) model, to ensure how many windows there is in the IFC Model.

## How the Script Addresses the Problem

The primary problem addressed by this script is the manual verification of architectural rules and design constraints. Normally, an architect or designer would need to manually inspect the BIM model for each element, which is time-consuming and prone to human error.

This script automates the process by applying predefined rules (in this case, the `windowRule`) to every window in the IFC model. The script:

1. Loads the IFC model using **ifcopenshell**.
2. Applies the `windowRule` to check each window's compliance.
3. Outputs the result of the rule check, by printing the amount of windows known as (IfcPlate) in this file.

## For Users Without BIM Expertise

This script is designed to be user-friendly, even for individuals without extensive knowledge of BIM. The script abstracts away complex BIM concepts and automates the rule-checking process, making it easier for non-BIM professionals to validate architectural models.

Basic knowledge of Python and how to run a script will suffice. The user needs to provide an IFC model as input, and the script will handle the rest.

## IFC Concepts

The script is built around Industry Foundation Classes (IFC), which is an open standard for BIM data. IFC is commonly used to exchange data in architecture, engineering, and construction (AEC) projects.

Key IFC concepts involved:
- **IFC File**: The input is an IFC file, which contains detailed information about a building's structure and components.
- **Window Elements**: The script focuses on analyzing elements classified as windows (`IfcWindow`) within the IFC schema.
- **Rules**: The `windowRule` function is used to apply specific constraints or checks to each window element.

## Further Analysis

This script can be expanded for further analysis, such as:

1. Energy calculations
2. U-value assessments
3. Verification of whether window-to-floor area exceeds 10%, as this creates a blaance between functionality, comfort and energy efficiency.

The data extracted can also include other building elements like walls, floors, and lighting fixtures. Such analyses can be beneficial for professionals working on indoor climate and daylight optimization. After analyzing this use case, the script can be adapted for other use cases, including architectural or installation projects.

