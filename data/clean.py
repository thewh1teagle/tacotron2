"""
Clean metadata.csv 
Replace numbers with correspond hebrew text
Replace symbols with correspond hebrew text
Remove prefix / suffix whitespaces


Make sure to fetch nakdimon model
wget https://github.com/elazarg/nakdimon/raw/master/models/Nakdimon.h5
"""

import csv 
import re
import json
import num2words # pip install num2words
import nakdimon # pip install git+https://github.com/thewh1teagle/nakdimon@feat/python-package

src_file = open('metadata.csv', 'r', encoding='utf-8')
dst_file = open('metadata_clean.csv', 'w', encoding='utf-8')
csv_reader = csv.reader(src_file, delimiter='|')
csv_writer = csv.writer(dst_file, delimiter='|')

symbols = {
    '%': 'אָחוּז'
}

invalid_sentences = {
    "שׂוֹר שָׁלֵם הִיא שִׁימְּשָׁה כְּמִסְפַּר שְׁתַּיִים שֶׁל וְסֶרְמָן, עַד שֶׁהוּא פָּרַשׁ מֵהָאִרְגּוּן בְּ-שְׁתַיים016, כְּשֶׁהוּגַּשׁ נֶגְדּוֹ כְּתַב אִישּׁוּם עַל מִרְמָה וַהֲפָרַת אֱמוּנִים, שֶׁבְּהֶמְשֵׁךְ גַּם הוּרְשַׁע בּוֹ.": "עָשׂוֹר שָׁלֵם הִיא שִׁמְּשָׁה כְּמִסְפַּר שְׁתַּיִם שֶׁל וַסֶרְמָן, עַד שֶׁהוּא פָּרַשׁ מֵהָאִרְגּוּן בִּשְׁנַת אַלְפַּיִם וְשֵׁשׁ עֶשְׂרֵה, כְּשֶׁהוּגַּשׁ נֶגְדּוֹ כְּתַב אִישׁוּם עַל מִרְמָה וַהֲפָרַת אֱמוּנִים, שֶׁבְּהֶמְשֵׁךְ גַּם הוּרְשַׁע בּוֹ."
}

def is_dirty(text: str) -> bool:
    pattern = re.compile(r'[{}0-9]'.format(re.escape(''.join(symbols.keys()))))
    return bool(pattern.search(text))

def replace_numbers_with_words(text, lang='he'):
    # Find all sequences of digits in the text
    numbers = re.findall(r'\d+', text)
    for number in numbers:
        text_number: str = num2words.num2words(int(number), lang=lang)
        text = text.replace(number, text_number)
        text = nakdimon.predict("Nakdimon.h5", text)
    return text

for line, row in enumerate(csv_reader, 1):
    file_id: str = row[0]
    _row1 = row[1] # It doesn't contains punctuation but we want them.
    text: str = row[2]
    if is_dirty(text) or any(i == text for i in invalid_sentences.keys()):
        # clean text
        text: str = replace_numbers_with_words(text)
        for key, value in symbols.items():
            text: str = text.replace(key, value)
        for invalid, correct in invalid_sentences.items():
            text = text.replace(invalid, correct)

    text = text.strip()
    csv_writer.writerow([file_id, text])


src_file.close()
dst_file.close()