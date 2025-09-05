# Translate English to Pig Latin

# def take the consonants together and add to the end of the word

# def stay the word form if begin with a vowel or "xr", "yt"

# de with have a "y" in the word, take it in the begin and take the consonants to the end

# def to add "ay" to the end of word


class PigLatin:
    def __init__(self, word: str) -> None:
        self.word = word

    def translate_word(self) -> str:
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
        if self.word.startswith(vowels) or self.word.startswith(("xr", "yt")):
            return self.word + "ay"

        # Rule 3: special case "qu"
        if self.word.startswith("qu"):
            return self.word[2:] + "quay"

        # Rule 3: consoante(s) + "qu"
        for i, letter in enumerate(self.word):
            if letter in vowels or (letter == "y" and i != 0):
                #  não pare no 'u' após 'q'
                if letter == "u" and i > 0 and self.word[i - 1] == "q":
                    continue
                return self.word[i:] + self.word[:i] + "ay"

        # (caso não encontre vogal nem 'y')
        return self.word + "ay"
