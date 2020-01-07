# How to access information from simple elements in XML

# Importing library to parse XML
import xml.etree.ElementTree as ET

# XML data
data = '''
<person>
    <name>Chuck</name>
    <phone type = "intl">
        +1 734 303 4456
    </phone>
    <email hide = "yes"/>
</person>
'''

# Parsing XML from string to XML
tree = ET.fromstring(data)

# Extracting information from XML
# Extracting string
print("Name:",tree.find('name').text)
print("Number:",tree.find('phone').text)

# Extracting attribute
print("Attribute:",tree.find('email').get('hide'))
