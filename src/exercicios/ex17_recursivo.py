def is_balanced(code: str) -> bool:
    """Verifica se brackets estão balanceados em uma string.

    Args:
        code: String contendo código com brackets/braces/parentheses

    Returns:
        True se todos os pares estão balanceados e aninhados corretamente,
        False caso contrário

    Examples:
        >>> is_balanced("{what is (42)}?")
        True
        >>> is_balanced("[text}")
        False
        >>> is_balanced("((()))")
        True
        >>> is_balanced("((())")
        False
    """
    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    def check(
        index: int,
        stack: list[str],
    ) -> bool:
        """Função recursiva auxiliar que verifica se a string está balanceada
        a partir de uma posição específica.

        Args:
            index (int): Posição atual na string `code` sendo analisada.
            stack (list[str]): Lista representando os símbolos de fechamento
                esperados até este ponto da análise.

        Returns:
            bool:
                - True se os caracteres a partir de `index` mantêm o
                balanceamento
                  correto de parênteses, colchetes e chaves.
                - False caso seja encontrado um fechamento incorreto ou
                  se a pilha não estiver vazia ao final.

        Detalhes:
            - Avança um caractere por chamada recursiva.
            - Se encontrar uma abertura (`(`, `[`, `{`), empilha o fechamento
            esperado.
            - Se encontrar um fechamento (`)`, `]`, `}`), verifica se
        corresponde
              ao topo da pilha.
            - Caracteres que não são delimitadores são ignorados.
            - O caso base ocorre quando `index` alcança o final da
            string `code`.
        """
        if index == len(code):
            return not stack

        char = code[index]

        if char in pairs:
            return check(
                index + 1,
                stack + [pairs[char]],
            )

        if char in pairs.values():
            return (
                bool(stack)
                and char == stack[-1]
                and check(
                    index + 1,
                    stack[:-1],
                )
            )

        return check(index + 1, stack)

    return check(0, [])
