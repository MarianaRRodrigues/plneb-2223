import re
import json

with open("termos_traduzidos.txt", encoding="UTF8") as file:
    text = file.read()

dici = {}

for line in text.split('\n'):
    term_translation = line.strip().split(" @ ")
    if len(term_translation) == 2:
        term, translation = term_translation
        dici[term] = f"en: {translation}"


with open('dictionary_translation2.json', 'w', encoding='UTF-8') as out:
    json.dump(dici, out, ensure_ascii=False, indent=4)
