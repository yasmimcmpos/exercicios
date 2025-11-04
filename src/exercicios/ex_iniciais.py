media = 0
n1 = n2 = n3 = n4 = 0.2
nome, age = "yasmim", 12
status = True

# Function Type()
print(type(media))
print(type(n2))
print(type(nome))
print(type(status))
print(type(1 + 2j))  # Complex number

# Function isinstance
a = 10
b = "Sol"
print(isinstance(b, int))  # False

a = 10
b = "Sol"
print(isinstance(a, int))  # True - aponta que já vai dar true

a = 10
b = "Sol"
print(isinstance(b, (int, float)))  # é um int ou um float

a = 40
c = 3
r = a * c
print(r)

# Operações

a = 10
b = 5

print(a / b)
print(a // b)
print(a % b)
print(a != b + 5)
