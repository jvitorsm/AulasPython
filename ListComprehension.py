#   List comprehension é uma estratégia de manipulação de lita em que não adição de termos, não seja 
#necessário tratamentos via laços.
#   Digamos que quero preencher os espaços de uma lista com o número de caracteres de uma palavra aleatória
# com: '_'. Podemos fazer isto através de um laço for:

import random

palavras = ["Abacaxi", "Borboleta", "Cachorro", "Diversidade", "Elefante","Futebol", "Girassol", "Harmonia", "Inovação", "Jardim","Ketchup", "Laranja", "Melodia", "Notável", "Ondulado","Pintura"]
palavra = random.choice(palavras)
lista = []
for letra in palavra:
    lista.append('_')
print(lista)

# Contudo podemos usar o for em uma List Comprehension
lista_2 = ['_' for letra in palavra]
print(lista)