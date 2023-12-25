# data_manipulation.py

# Task 1: Data Preparation
persons = [
    {"name": "Alice", "age": 28, "city": "New York"},
    {"name": "Bob", "age": 22, "city": "San Francisco"},
    {"name": "Charlie", "age": 30, "city": "Los Angeles"},
    {"name": "David", "age": 18, "city": "Chicago"},
]

# Task 2: Filtering
filtered_persons = [person for person in persons if person["age"] >= 25]

# Task 3: Sorting
sorted_persons = sorted(filtered_persons, key=lambda x: x["city"])

# Task 4: Output
for person in sorted_persons:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")

# Comments:
# Task 1 creates a list of dictionaries representing persons with attributes.
# Task 2 filters out persons under the age of 25 using a list comprehension.
# Task 3 sorts the remaining persons based on their city in alphabetical order.
# Task 4 prints the final list of persons to the console.
