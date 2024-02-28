import json

# Reading JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)  # This will display the content of the data.json file as a Python dictionary.
