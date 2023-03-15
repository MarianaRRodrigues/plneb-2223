import re


file = open('dicionario_medico.txt', encoding="UTF8")
text = file.read()



#resolver os casos em que há mudança de página, ou seja, a palavra e a designação ficam em páginas diferentes
# se não tem ponto final e tem há mudança de página 

text = re.sub(r'(([^\.])\n\n)\f', r'\2\n', text)

text = re.sub(r'\f', '', text)

#Quando a frase da descrição é separada por \n\n ou mais 
# Se tiver dois ou mais \n vão ser substituidos por um \n

text = re.sub(r'\n\n+', r'\n', text)


# 1º grupo de captura: (.+) -- apanha as designações
# 2º grupo de captura: ((\n.+)+) -- apanha todas as linhas
# 3º grupo de captura: (\n.+) -- apanha linha a linha 
# ?: -- silencia grupo de captura, serve para não aparecer linha a linha no tuplo, mas tudo junto
entries = re.findall(r'\n\n(.+)((?:\n.+)+)', text)

print(entries[30:40])

# criação de uma nova lista para remover o \n da descrição de cada termo

new_entries = []

'''for designation, description in entries:
    description = description.strip()
    new_entries.append((designation, description)) '''

# Outra maneira de fazer a mesma coisa

new_entries = [(designation, description.strip()) for designation, description in entries]

print(new_entries[10])

file.close()


# Criação do ficheiro html

html = open('dicionario_medico.html', 'w', encoding='UTF8')

header = '''<html>
                <head>
                    <meta charset="utf-8"/>
                    <title>Dicionário Médico</title>
                </head>
                <body>
        '''

body = ''
for designation, description in new_entries:
    body += '<b>' + designation + '</b>'
    body += '<p>' + description + '</p>' + '<hr>'

footer = '''</body>
        </html>'''

html.write(header + body + footer)

html.close()