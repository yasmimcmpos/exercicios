# Implemente operações básicas de lista.

# Em linguagens funcionais, liste operações como , , e são muito comuns.
# Implemente uma série de operações básicas de lista,
# sem usar funções existentes. length map reduce

# O número e os nomes exatos das operações a serem implementadas dependerão
# do controle para evitar conflitos com nomes existentes,
# mas as operações gerais que você implementará incluem:

# append (dadas duas listas, adicione todos os
# itens da segunda lista ao final da primeira lista);

# concatenate (dada uma série de listas, combine todos os itens em todas
# as listas em uma lista nivelada);

# filter (dado um predicado e uma lista, retorna a lista de todos os itens
# para os quais é Truepredicate(item));

# length (dada uma lista, retorna o número total de itens dentro dela);

# map (dada uma função e uma lista, retorna a lista dos resultados da aplicação
# em todos os itensfunction(item));

# foldl (Dada uma função, uma lista e um acumulador inicial, dobre (reduza)
# cada item no acumulador da esquerda);

# foldr (dada uma função, uma lista e um acumulador inicial, dobre (reduza)
# cada item no acumulador da direita);

# reverse (dada uma lista, retorna uma lista com todos os itens originais,
# mas na ordem inversa).

# Observe que a ordem na qual os argumentos são passados para as
# funções de dobra (, ) é significativa.
# foldl foldr


def exer1(lista1, lista2) -> None:
    for item in lista2:
        lista_nova = lista1 + [item]
        print(lista_nova)
