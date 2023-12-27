from datetime import datetime

# Create a datetime object
my_datetime = datetime.now()

# Format the datetime object as a string with both date and time
formatted_datetime = my_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Print the result
print("Original datetime:", my_datetime)
print("Formatted datetime:", formatted_datetime)