# https://exercism.org/tracks/python/exercises/acronym
# Convert a phrase to its a acronym
import re


def convert(phrase: str) -> str:
    """Converte uma frase em um acrônimo.

    Args:
        phrase (str): Frase de entrada a ser convertida em acrônimo.

    Returns:
        str: Acrônimo formado pelas iniciais das palavras da frase.

    Obs:
        Regras aplicadas:
        1-Substitui hífens ("-") por espaços, tratando palavras compostas
       como palavras separadas.

        2-Remove caracteres especiais e pontuações, mantendo apenas letras
       e espaços.

        3-Separa a frase em palavras utilizando espaços como delimitador.

        4-Extrai a primeira letra e converte todas as letras extraídas para maiúsculas.

        5-Junta as letras em uma única string representando o acrônimo final.

        r - não interpretar
        A-Az-z - Letras maiúsculas e minúsculas
        \s - espaços, tabs..

    """
    phrase = phrase.replace("-", " ")

    phrase = re.sub(r"[^A-Za-z\s]", "", phrase)

    words = phrase.split()

    acronym_letters = [word[0].upper() for word in words]

    return "".join(acronym_letters)
