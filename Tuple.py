#   Assim como listas e strings, Tuples são sequencias de valores. Contudo essas sequencias são imutáveis
#   São usadas para proverem listas de valores que logicamente não tem sentido a mutabilidade,como por
#exemplo usa-las em questionários em listagem de estados ou uma lista de dias da semana.
#   Listas são definadas por pares de colchete, enquato tuples por pares de parênteses

lista = [9,2,3,4,5,3]
lista.append(8)
print(lista)
print(len(lista))
print(lista.count(3))
lista.pop()
print(lista)

#   Como podemos ver a lista possui vários atributos para a manipulação, não obstante os tuples tambem possuem
#atributos, porem mais ligados a averiguação e retorno do que necessariamente de manipulação

Tuple = ('Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab')
print(Tuple)
#   >>Tuple.append('Novo Dia')
#   <<AttributeError: 'tuple' object has no attribute 'append'
print(len(Tuple))
print(Tuple.count('Seg'))
#   >>Tuple.pop()
#   <<AttributeError: 'tuple' object has no attribute 'pop'



#   PARA MAIS INFORMAÇÕES CONSULTE A DOCUMENTAÇÃO: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences


