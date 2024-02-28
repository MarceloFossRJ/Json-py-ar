import json

# Data to be written
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Writing JSON data into a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)