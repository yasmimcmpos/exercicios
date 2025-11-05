num = 1
while num <= 100:
    print(num)
    num += 50
print("Laço encerrado")


nome = None
while True:
    print("Seu nome:, ou x para parar:")
    nome = input()
    if nome == "x" or nome == "X":
        break
    print(f"bem vindo, {nome}")


# Laço For -
# for item in sequencia:
# para cada valor na sequencia um conjunto de instruções é executado até
# finalizar a sequencia


lista = [2, 3, 5, 8, 0, 4, 65]
for item in lista:
    print(item)

frase = ["boston", "é", "legal"]
for palavra in frase:
    print(palavra)

for numero in range(0, 11, 2):
    print(numero)

for numero in range(10):
    print(numero)


nome = input("Digite seu nome:")
for x in range(10):
    print(f"{x+1} {lista_nomes}")


# Caso queira colocar um nome em cada linha

lista_nomes = []
for i in range(10):
    nome = str(input("Nomes:"))
    lista_nomes.append(nome)

for i, nome in enumerate(lista_nomes, start=1):
    print(f"{i}.{nome}")

# estrutura do enumerate: for indice, lista in enumerate(lista, start=1):
