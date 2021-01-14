# Add dependencies
import csv
import os

# Assign variable to load the file from a path.
file_to_load = os.path.join("resources", "election_results.csv")

# Assign Variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# read and print header row.
    headers = next(file_reader)
    print(headers)
