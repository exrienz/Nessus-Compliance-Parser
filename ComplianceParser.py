import csv
import json
import os

def delete_duplicates(data):
    unique_rows = []
    unique_set = set()
    for entry in data:
        # Convert the entry to a tuple and check if it's in the set
        entry_tuple = tuple(entry.values())
        if entry_tuple not in unique_set:
            unique_set.add(entry_tuple)
            unique_rows.append(entry)
    return unique_rows

def convert_csv_to_json(csv_file_path, json_file_path):
    data = []

    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)

    with open(json_file_path, 'w') as jsonfile:
        jsonfile.write(json.dumps(data, indent=2))

def process_json_file(json_file_path):
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    filtered_data = [
        {
            "Host": process_host(entry.get("Host", "")),
            "Risk": entry.get("Risk", ""),
            "Description_Title": entry.get("Description", "").split(':')[0].strip('"'),
            "See_Also": entry.get("See Also", "")
        }
        for entry in json_data
        if entry.get("Risk") == "FAILED"
    ]

    filtered_data_without_quotes = [
        {
            "Host": entry["Host"],
            "Risk": entry["Risk"],
            "Description_Title": entry["Description_Title"].replace("'", "").replace('"', ''),
            "See_Also": entry["See_Also"]
        }
        for entry in filtered_data
    ]

    return filtered_data_without_quotes

def process_host(host):
    # Remove everything starting from "-config", ".", or "-2023"
    host = host.split('-config')[0].split('.')[0].split('-2023')[0]
    return host

# Get the current working directory
current_directory = os.getcwd()

# List all CSV files in the current folder
csv_files = [file for file in os.listdir(current_directory) if file.endswith(".csv")]

# Initialize an empty list to store the combined data
combined_data = []

# Process each CSV file
for csv_file in csv_files:
    # Form the full paths for CSV and JSON files
    csv_file_path = os.path.join(current_directory, csv_file)
    json_file_path = os.path.splitext(csv_file_path)[0] + ".json"

    # Convert CSV to JSON
    convert_csv_to_json(csv_file_path, json_file_path)

    # Process JSON file
    filtered_data = process_json_file(json_file_path)

    # Append the filtered data to the combined_data list
    combined_data.extend(filtered_data)

# Delete duplicate rows
combined_data = delete_duplicates(combined_data)

# Prompt the user for the final CSV filename
user_input_filename = input("Enter the final CSV filename (without extension): ")
csv_filename = f"{user_input_filename}.csv"
csv_file_path = os.path.join(current_directory, csv_filename)

# Check if the file already exists and delete it
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
    print(f"Old file '{csv_filename}' deleted.")

# Writing the combined and unique data to the final CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ["Host", "Risk", "Description_Title", "See_Also"]
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header
    csvwriter.writeheader()

    # Write the data
    csvwriter.writerows(combined_data)

print(f"Combined and unique data saved to {csv_filename}")
