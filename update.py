import json

# Reading the data
with open('data.json', 'r') as file:
    data = json.load(file)

# Modifying the data
data['age'] = 31  # Updating the age
data['email'] = 'john.doe@example.com'  # Adding a new key-value pair

# Writing the modified data back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# conditional update

# Define the condition for the update
name_to_update = "John Doe"
new_city = "Los Angeles"

# Load the data
with open('data.json', 'r') as file:
    data = json.load(file)

# Check each user and update the city if the name matches
for user in data['users']:  # Assuming the data is a dictionary with a 'users' list
    if user['name'] == name_to_update:
        user['city'] = new_city
        break  # Assuming only one user with this name, we can break after finding the match

# Write the updated data back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)