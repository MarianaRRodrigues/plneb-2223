import re
import json

ficheiro = open("dicionario_medico.xml","r",encoding="utf-8")
text = ficheiro.read()


def limpa(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


#Remover </page>
text = re.sub(r"</?page.*>", "", text)

#Remover o text
text = re.sub(r"</?text.*?>", "",text)

# Ficamos como uma lista de tupulos
lista = re.findall(r"<b>(.*)</b>([^<]*)", text)

#strip limpa alguns /n
lista = [(designacao, limpa(descricao)) for designacao, descricao in lista] 

dicionario = dict(lista)

#Escrever
out= open("dicionario_medico.json", "w",encoding="utf-8")

json.dump (dicionario, out, ensure_ascii=False, indent=4) #1º argumento- o que queremos copiar 2º argumento: onde queremos guardar


out.close()

print(lista)



