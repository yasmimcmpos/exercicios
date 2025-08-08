# Create an implementation of the rotational cipher, also sometimes called
# the Caesar cipher.
# .index - serve para encontrar a posição de uma string ou lista
# wrap around - útil para alfabeto, listas circulares ou relógios,
#


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char = "H"
key = 3
atual_position = alphabet.index(char)
new_position = atual_position + key
new_char = alphabet[new_position]
print(new_position, new_char)
