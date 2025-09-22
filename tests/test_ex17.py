from exercicios.ex17 import is_balanced


def test_balanced_basic() -> None:
    # Testa casos básicos balanceados
    assert is_balanced("{what is (42)}?") is True
    assert is_balanced("()") is True
    assert is_balanced("[]") is True
    assert is_balanced("{}") is True


def test_unbalanced_basic() -> None:
    # Testa casos básicos não balanceados
    assert is_balanced("[text}") is False
    assert is_balanced("(]") is False
    assert is_balanced("{)") is False


def test_nested_balanced() -> None:
    # Testa aninhamento correto
    assert is_balanced("({[]})") is True
    assert is_balanced("[{()}]") is True
    assert is_balanced("((()))") is True
    assert is_balanced("{[()]}") is True


def test_nested_unbalanced() -> None:
    # Testa aninhamento incorreto
    assert is_balanced("([)]") is False
    assert is_balanced("{[}]") is False
    assert is_balanced("((())") is False
    assert is_balanced("())") is False


def test_empty_and_single_chars() -> None:
    # Testa casos extremos
    assert is_balanced("") is True
    assert is_balanced("hello world") is True
    assert is_balanced("(") is False
    assert is_balanced(")") is False


def test_mixed_with_text() -> None:
    # Testa com texto misturado
    assert is_balanced("func(param1, param2)") is True
    assert is_balanced("array[index] + dict{key}") is True
    assert is_balanced("if (condition) { do_something(); }") is True
    assert is_balanced("unclosed function(param") is False
