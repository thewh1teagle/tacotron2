"""
Fix wav file paths in latin metadata
"""


import csv
import os

# Read the original data
with open('metadata_latin.csv', 'r', encoding='utf-8') as src_file:
    csv_reader = csv.reader(src_file, delimiter='|')
    rows = list(csv_reader)  # Read all rows into a list

# Modify the file paths and prepare the data for writing
modified_rows = []
for row in rows:
    file_id: str = row[0]
    text: str = row[1]
    file_id = f'{file_id}.wav'
    modified_rows.append([file_id, text])

# Write the modified data back to the same file
with open('metadata_latin.csv', 'w', encoding='utf-8', newline='') as src_file:
    csv_writer = csv.writer(src_file, delimiter='|')
    csv_writer.writerows(modified_rows)
