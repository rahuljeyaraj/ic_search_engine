import json

# Load data
with open("db.json") as f:
    data = json.load(f)

# Get user input
user_voltage = input("Enter required output voltage (e.g., 5V): ")

# Search logic
results = []

for comp in data:
    if comp["output_voltage"] == user_voltage:
        results.append(comp)

# Print results
if results:
    print("\nMatching components:")
    for r in results:
        print(r["name"])
else:
    print("\nNo matching components found")