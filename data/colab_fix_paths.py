from pathlib import Path
import csv

# Define paths
CUR_PATH = Path(__file__).parent
TRAIN_PATH = CUR_PATH / 'train_data'
TRAIN_METADATA_PATH = TRAIN_PATH / 'metadata.csv'
VALIDATION_PATH = CUR_PATH / 'validation_data'
VALIDATION_METADATA_PATH = VALIDATION_PATH / 'metadata.csv'


def update_metadata(metadata_path):
    with open(metadata_path, 'r', encoding='utf-8') as metadata_file:
        csv_reader = csv.reader(metadata_file, delimiter='|')
        data = list(csv_reader)
        for row in data:
            file_path = row[0]
            name = Path(file_path).name
            new_path = metadata_path.parent / name
            row[0] = new_path

    with open(metadata_path, 'w', encoding='utf-8', newline='') as metadata_file:
        csv_writer = csv.writer(metadata_file, delimiter='|')
        csv_writer.writerows(data)

# Update train metadata
update_metadata(TRAIN_METADATA_PATH)

# Update validation metadata
update_metadata(VALIDATION_METADATA_PATH)

print('Paths Updated')