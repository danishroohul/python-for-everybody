# How to access data from complex elements in XML

# Import library to parse xml
import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x = "2">
            <name>Chuck</name>
            <id>007</id>
        </user>
        <user x = "7">
            <name>Danny</name>
            <id>420</id>
        </user>
    </users>
</stuff>
'''

tree = ET.fromstring(data)
lst = tree.findall('users/user')
print("Number of users:",len(lst),end="\n\n")

for item in lst:
    print("Name:",item.find("name").text)
    print("ID:",item.find("id").text)
    print("Attribute:",item.get('x'),end="\n\n")
