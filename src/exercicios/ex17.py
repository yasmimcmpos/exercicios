from typing import List


def is_balanced(code: str) -> bool:
    """
    Verifica se brackets, braces e parentheses estão balanceados em uma string.

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
    stack: List[str] = []  # Pilha - LIFO
    opening = {"(": ")", "[": "]", "{": "}"}
    closing = {")", "]", "}"}

    for char in code:
        if char in opening:
            stack.append(opening[char])
        elif char in closing:
            if not stack or char != stack.pop():
                return False
    return not stack
