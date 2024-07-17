"""
transliteration using https://github.com/charlesLoder/hebrew-transliteration
Using JSPyBridge. hacky. but works. https://github.com/extremeheat/JSPyBridge
pip3 install javascript
"""
from javascript import require
import csv 
import re
import json
import num2words # pip install num2words
import nakdimon # pip install git+https://github.com/thewh1teagle/nakdimon@feat/python-package

transliteration = require("hebrew-transliteration")

src_file = open('metadata_clean.csv', 'r', encoding='utf-8')
dst_file = open('metadata_latin.csv', 'w', encoding='utf-8')
csv_reader = csv.reader(src_file, delimiter='|')
csv_writer = csv.writer(dst_file, delimiter='|')


for line, row in enumerate(csv_reader, 1):
    file_id: str = row[0]
    text: str = row[1]
    text = transliteration.transliterate(text)
    csv_writer.writerow([file_id, text])

