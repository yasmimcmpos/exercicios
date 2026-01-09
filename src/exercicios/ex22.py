# https://projecteuler.net/problem=11
# For the Grid.csv find the product of the four adjacent numbers in the same
# direction (up, down, left, right, or diagonally) in different directions.
# Qual é o maior produto de numeros adjacentes na mesma direção


# Minha  primera Lógica para resolver:
# 1 função que leia todos os numeros e os separe em grupos de 4 na diagonal, vertical e horizontal
# usando coordenadas
# eu calculo o produto de cada grupo e Só guardo o grupo se ele bater o maior produto atual.
# No meu arquivo de test apenas verifico se meu maior resultado é fruto do produto.


# Uma função percorre o grid usando coordenadas.
# Para cada posição e direção válida, ela forma um grupo conceitual de 4 números.
# O produto é calculado imediatamente.
# Se for maior que o atual, o produto e o grupo são armazenados.
# Ao final, a função retorna o maior produto e seu grupo.

# Varivel para o mairo numero =0
# Pecorrer a posição
# verificar o limite(4 posiçoes validas)
# Calcula o produto x
# Compara com o maior encontrado e armazena se for maior
# retorna o produto
