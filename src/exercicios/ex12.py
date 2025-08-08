# Create an implementation of the rotational cipher, also sometimes called
# the Caesar cipher.
# .index - serve para encontrar a posição de uma string ou lista
# wrap around - útil para alfabeto, listas circulares ou relógios,


def cesar(letter: str, key: int) -> str:
    """Applies Caesar cipher to a single letter.

    Args:
        letter (str): A single alphabetic character.
        key (int): The shift value for the cipher.

    Returns:
        str: The encrypted character.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter = letter.upper()

    if letter in alphabet:
        atual_position = alphabet.index(letter)
        new_position = (atual_position + key) % len(alphabet)  # 26
        return alphabet[new_position]
    else:
        return letter
