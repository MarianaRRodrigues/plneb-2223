#Exercícios
import collections
import unicodedata

#Pergunta 1 - Programa que pergunta ao utilizador o nome e imprime em maiúsculas.

username= input('Introduza o seu nome ');
print("Nome em maiúsculas:" , username.upper())


#Pergunta 2 - Função que recebe array de números e imprime números pares.

def numeropar():

    array = [1,2,3,4,5,6,7,8,9,10]
    for i in array:
        if i% 2 == 0:
            print("O número", i, "é par")

numeropar()

#Pergunta 3 - Função que recebe nome de ficheiro e imprime linhas do ficheiro em ordem inversa.

filename = input("Escreva o nome do ficheiro ")

def printlinesreverseorder(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()
        reverselines = lines[::-1]

        for line in reverselines:
            print(line.strip())

printlinesreverseorder(filename)

#Pergunta 4 - Função que recebe nome de ficheiro e imprime número de ocorrências das 10 palavras mais frequentes no ficheiro.

def occurrences10mostfreqwords(filename):
    with open(filename, 'r') as file:
        file_text = file.read()
        words = file_text.split()
        count = collections.Counter(words) #Counter - conta a frequência de cada palavra na lista palavras
        frequent_words = count.most_common(10)
        #print(frequent_words)

        for word, word_frequecy in frequent_words:
            print(f'{word}: {word_frequecy} ocorrências')

occurrences10mostfreqwords(filename)


# Pergunta 5 - Função que recebe um texto como argumento e o ”limpa”: separa palavras e pontuação com espaços, converte para minúsculas, remove acentuação de caracteres, etc.

import re

text = input("Insira o texto ")

def clear_text(text ):
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII') #  remove acentuação de caracteres
    text = text.lower()  # converte para minúsculas
    text = re.sub(r'[^\w\s]', ' ', text) # separa palavras e pontuação com espaços
    print('Texto final', text)

clear_text(text)

# ---------------------------------------------------------------------------------------------------------------------------
#Exercícios

string= input('Introduza uma string ')

# Pergunta 1 - Create a function that given a string “s”, reverse it.

def reverse_string(string):
    print("A string invertida é: ", string[::-1])

reverse_string(string)


# Pergunta 2 - Create a function that given a string “s”, returns how many “a” and “A” characters are present in it.

def characters_present(string):
    count = 0
    characters = set("aA")

    for i in string:
        if i in characters:
            count = count + 1
    print('O número de caracteres a e A que estão presentes é:', count)

characters_present(string)

# Pergunta 3 - Create a function that given a string “s”, returns the number of vowels there are present in it.


def vowelscount(string):
    count = 0
    vowel = set("aeiouAEIOU")

    for l in string:
        if l in vowel:
            count= count + 1
    print('O número de vogais é: ', count)

vowelscount(string)

# Pergunta 4 - Create a function that given a string “s”, convert it into lowercase.

def convert_lowercase(string):
    print("Conversão em minúsculas:", string.lower())

convert_lowercase(string)

# Pergunta 5 - Create a function that given a string “s”, convert it into uppercase.

def convert_uppercase(string):
    print("Conversão em maiúsculas:", string.upper())

convert_uppercase(string)