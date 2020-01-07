# importing json library
import json

# Json data
data = '''
[
    {
    "name" : "Chuck",
    "id" : "007",
    "x" : "2"
    },
    {
    "name" : "Danny",
    "id" : "420",
    "x" : "7"
    }
]
'''

# Get json data from string (loads = load from string)
info = json.loads(data)

print("Number of users:",len(info),end="\n\n")

# info is a list, we loop through list to extract information from dictionaries
for item in info:
    print("Name:", item["name"])
    print("ID:", item["id"])
    print("Attribute:", item["x"],end="\n\n")
