# importing json library
import json

# Json data
data = '''
{
"name" : "Chuck",
"phone" :
        {
        "type" : "intl",
        "number" : "+1 734 303 4456"
        },
"email" :
        {
        "hide" : "yes"
        }
}
'''

# Get json data from string (loads = load from string)
info = json.loads(data)

# info is now a dictionary, extract information like how we extract in dictionary
print("Name:",info["name"])
print("Number:",info["phone"]["number"])
print("Hide:",info["email"]["hide"])
