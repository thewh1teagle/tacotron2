from pathlib import Path
import csv
import random
import shutil

# Define paths
CUR_PATH = Path(__file__).parent
TRAIN_PATH = CUR_PATH / 'train_data'
TRAIN_METADATA_PATH = TRAIN_PATH / 'metadata.csv'
VALIDATION_PATH = CUR_PATH / 'validation_data'
VALIDATION_METADATA_PATH = VALIDATION_PATH / 'metadata.csv'
WAVS_PATH = CUR_PATH / 'resampled'
METADATA_PATH = CUR_PATH / 'metadata_latin.csv'

# Ensure the directories exist
TRAIN_PATH.mkdir(exist_ok=True)
VALIDATION_PATH.mkdir(exist_ok=True)

# Define validation percentage
VALIDATION_PERCENTAGE = 5 / 100.0  # 5%


# Copy wav files to the respective directories
def copy_wav_files(data, destination_path):
    for row in data:
        file_id = row[0]
        wav_src = WAVS_PATH / f"{file_id}"
        wav_dest = destination_path / f"{file_id}"
        if wav_src.exists():
            shutil.copy(wav_src, wav_dest)


# Read the metadata
with open(METADATA_PATH, 'r', encoding='utf-8') as latin_file:
    csv_reader = list(csv.reader(latin_file, delimiter='|'))
    total_lines = len(csv_reader)
    validation_size = int(total_lines * VALIDATION_PERCENTAGE)

    # Shuffle data and split into train and validation sets
    random.shuffle(csv_reader)
    validation_data = csv_reader[:validation_size]
    train_data = csv_reader[validation_size:]

# Ensure directories exist before copying
TRAIN_PATH.mkdir(parents=True, exist_ok=True)
VALIDATION_PATH.mkdir(parents=True, exist_ok=True)

# Copy train and validation wav files
copy_wav_files(train_data, TRAIN_PATH)
copy_wav_files(validation_data, VALIDATION_PATH)

# Write validation metadata
with open(VALIDATION_METADATA_PATH, 'w', encoding='utf-8', newline='') as validation_file:
    csv_writer = csv.writer(validation_file, delimiter='|')
    for row in validation_data:
        file_id = row[0]
        absolute_path = str((Path(VALIDATION_PATH) / file_id).absolute())
        row[0] = absolute_path
    csv_writer.writerows(validation_data)

# Write train metadata
with open(TRAIN_METADATA_PATH, 'w', encoding='utf-8', newline='') as train_file:
    csv_writer = csv.writer(train_file, delimiter='|')
    for row in train_data:
        file_id = row[0]
        absolute_path = str((Path(TRAIN_PATH) / file_id).absolute())
        row[0] = absolute_path
    csv_writer.writerows(train_data)




print("Data split complete. Train and validation data have been created.")



