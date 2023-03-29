from deep_translator import GoogleTranslator

import json

translator = GoogleTranslator(source='pt', target='en') 


file_in = open("dicionario_medico.json",  encoding="UTF8")

dici = json.load(file_in)

new_dici = {}

for designation, description in dici.items():
    en_translation = translator.translate(designation)
    print(en_translation)
    new_dici[designation] = {
                            "des": description,
                            "en": translator.translate(designation)
                            }

file_out = open("dictionary_translation.json")
json.dump(new_dici, ensure_ascii=False, indent=4)
file_out.close()

#print(translator)
