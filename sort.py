import csv

# Read the CSV file
print("Enter the csv file-path to sort by frequency:")
input_file = input()
print("Enter the output name for the sorted file:")
output_file = input()
with open(input_file, mode='r') as file:
    reader = csv.DictReader(file)
    problems = list(reader)

# Function to clean and convert the "Frequency %" value
def clean_frequency(frequency):
    return float(frequency.replace('%', '').replace(';', ''))

# Sort the problems by "Frequency %" in decreasing order
problems_sorted = sorted(problems, key=lambda x: clean_frequency(x['Frequency']), reverse=True)

# Write the sorted data to a new CSV file
with open(output_file, mode='w', newline='') as file:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(problems_sorted)

print(f'Sorted data has been written to {output_file}')
