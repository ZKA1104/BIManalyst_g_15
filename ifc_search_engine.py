import ifcopenshell
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the IFC file (update "your_file.ifc" with the actual file name)
ifc_file_path = "your_file.ifc"
try:
    ifc_file = ifcopenshell.open(ifc_file_path)
except Exception as e:
    print(f"Error loading IFC file: {e}")
    ifc_file = None

# Function to search for entities by type and filter by properties if specified
def search_ifc_entities(entity_type=None, property_name=None, property_value=None):
    if not ifc_file:
        return []

    results = []
    # Retrieve entities of the specified type or all entities if no type is given
    entities = ifc_file.by_type(entity_type) if entity_type else ifc_file.by_type("IfcProduct")

    # Filter entities by property if specified
    for entity in entities:
        if property_name and property_value:
            # Access the properties set to match the name-value pair
            if entity.HasProperties:
                for prop in entity.HasProperties:
                    if prop.Name == property_name and str(prop.NominalValue) == property_value:
                        results.append(entity)
                        break
        else:
            results.append(entity)
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        # Get search parameters from form
        entity_type = request.form.get('entity_type')
        property_name = request.form.get('property_name')
        property_value = request.form.get('property_value')
        
        # Search IFC entities based on the form inputs
        results = search_ifc_entities(entity_type, property_name, property_value)
    
    # Render the HTML template with search results
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)



