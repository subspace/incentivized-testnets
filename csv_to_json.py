import csv
import json

input_file = 'Final_farming_rewards.csv'
output_file = 'genesis_allocations.json'

allocations = []

def parse_number(s):
    # Remove commas and decimal point
    s = s.replace(',', '').replace('.', '')
    # Pad with zeros: token_decimals - precision
    return int(s)

with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row if it exists
    for row in csvreader:
        address = row[0].strip()
        balance = parse_number(row[1])
        if balance > 0:
            allocations.append([address, balance])

with open(output_file, 'w') as jsonfile:
    json.dump(allocations, jsonfile, separators=(',', ':'))

print(f"Conversion complete. JSON data written to {output_file}")