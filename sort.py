import csv

# Read the CSV file
input_file = 'google.csv'
output_file = 'sorted_google.csv'

with open(input_file, mode='r') as file:
    reader = csv.DictReader(file)
    problems = list(reader)

# Function to clean and convert the "Frequency %" value
def clean_frequency(frequency):
    return float(frequency.replace('%', '').replace(';', ''))

# Sort the problems by "Frequency %" in decreasing order
problems_sorted = sorted(problems, key=lambda x: clean_frequency(x['Frequency %']), reverse=True)

# Write the sorted data to a new CSV file
with open(output_file, mode='w', newline='') as file:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(problems_sorted)

print(f'Sorted data has been written to {output_file}')
