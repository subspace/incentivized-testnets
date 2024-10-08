import csv
import json

input_file = 'Final_farming_rewards.csv'
output_file = 'genesis_allocations.json'
sheet_precision = 2  # Number of decimal places in the CSV
token_decimals = 18  # Total number of decimals for the token

allocations = []

def parse_number(s, precision):
    # Remove commas and decimal point
    s = s.replace(',', '').replace('.', '')
    # Pad with zeros: token_decimals - precision
    return s + '0' * (token_decimals - precision)

with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row if it exists
    for row in csvreader:
        address = row[0].strip()
        balance = parse_number(row[1], sheet_precision)
        allocations.append({
            "address": address,
            "balance": balance
        })

with open(output_file, 'w') as jsonfile:
    json.dump(allocations, jsonfile, indent=2)

print(f"Conversion complete. JSON data written to {output_file}")