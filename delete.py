import json

# Reading the data
with open('data.json', 'r') as file:
    data = json.load(file)

# Deleting the 'city' key-value pair
del data['city']

# Writing the updated data back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# conditional delete

# Define the condition for deletion
age_threshold = 30

# Load the data
with open('data.json', 'r') as file:
    data = json.load(file)

# Use a list comprehension to filter out users over the age threshold
data['users'] = [user for user in data['users'] if user['age'] <= age_threshold]

# Write the updated data back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

