import json
import re

#open file
file = open("dicionario_medico.json", encoding="utf-8")
lista = json.load(file)

#print(lista)
file.close()


txtfile = open("LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding="utf-8")
txt= txtfile.read()
print(txt)

txt = re.findall(r"<b>(.+?)</b>",r" ", txt)

txtfile.close()

# Criação do ficheiro html

html = open('livro_doenças_aparelho_dig', 'w', encoding='UTF8')

header = '''<html>
                <head>
                    <meta charset="utf-8"/>
                    <title>Livro de Doenças </title>
                </head>
                <body>
        '''

body ='' + txt

footer = '''</body>
        </html>'''

html.write(header + body + footer)

html.close()
