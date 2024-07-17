"""
Check that all the wav files exists
Check that the characters are valid in metadata_transliterated.csv
"""

import csv 
from pathlib import Path


# See symbols.py
_punctuation = "!',-.?:\" "
_special = '-'
_letters = 'abdeghiklmnopqrstwyzâêîôûāăēĕōŏśšūǝʾʿׁḥṣṭ”'
valid_symbols = list(_special) + list(_punctuation) + list(_letters) # + _arpabet

# Read metadata
src_file = open('metadata_latin.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(src_file, delimiter='|')

missing_files = []
invalid_sentences = []
for line, row in enumerate(csv_reader, 1):
    file_id: str = row[0]
    text: str = row[1]
    path = Path(f'waves/{file_id}')
    if not path.exists():
        missing_files.append(path)
    for c in text:
        if c not in valid_symbols:
            invalid_sentences.append(text)
            break


if missing_files:
    print('❌ Missing files!', missing_files)

if invalid_sentences:
    print('❌ Invalid sentences!', len(invalid_sentences))

if not missing_files and not invalid_sentences:
    print("✅ Looks good!")

