# Translate English to Pig Latin

# def take the consonants together and add to the end of the word

# def stay the word form if begin with a vowel or "xr", "yt"

# de with have a "y" in the word, take it in the begin and take the consonants to the end

# def to add "ay" to the end of word


class PigLatin:
    def __init__(self) -> None:
        # Método __init__ vazio porque não precisamos inicializar nada
        pass

    def translate_word(self, word: str) -> str:
        """A class to translate English words or phrases into Pig Latin.

        Args:
            word (str): The word to translate.

        Returns:
            str: The translated Pig Latin word.

        Observations: "word.startswith" is a Python's string method. Ele serve
        para verificar se uma string começa com um determinado prefixo.

        The use of [i:] and [:i] - significa pegue a string word do índice i
        até o fim" ou o contrário.

        Examples:
        (word[0:])  "python"  (começa no 0 e vai até o fim)
        (word[2:])  "thon"
        """
        vowels = ("a", "e", "i", "o", "u")
        # Rule 1: begin with a vowels and "xr"/"yt"
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            return word + "ay"

        for i, letter in enumerate(word):
            if letter in vowels or (letter == "y" and i != 0):
                return word[i:] + word[:i] + "ay"

        # (caso não encontre vogal nem 'y')
        return word + "ay"

    # def translate(self, text: str) -> str:
    #     """This method splits the input text into words, translates each word
    #     using `translate_word`, and then joins them back into a phrase.

    #     Args:
    #         text (str): The English phrase to translate.

    #     Returns:
    #         str: The translated Pig Latin phrase.
    #     """
    #     return " ".join(self.translate_word(word) for word in text.split())
