from exercicios.ex17 import is_balanced


def test_balanced_basic() -> None:
    # Testa casos básicos balanceados
    assert is_balanced("{what is (42)}?")
    assert is_balanced("()")
    assert is_balanced("[]")
    assert is_balanced("{}")


def test_unbalanced_basic() -> None:
    # Testa casos básicos não balanceados
    assert not is_balanced("[text}")
    assert not is_balanced("(]")
    assert not is_balanced("{)")


def test_nested_balanced() -> None:
    # Testa aninhamento correto
    assert is_balanced("({[]})")
    assert is_balanced("[{()}]")
    assert is_balanced("((()))")
    assert is_balanced("{[()]}")


def test_nested_unbalanced() -> None:
    # Testa aninhamento incorreto
    assert not is_balanced("([)]")
    assert not is_balanced("{[}]")
    assert not is_balanced("((())")
    assert not is_balanced("())")


def test_empty_and_single_chars() -> None:
    # Testa casos extremos
    assert is_balanced("")
    assert is_balanced("hello world")
    assert not is_balanced("(")
    assert not is_balanced(")")


def test_mixed_with_text() -> None:
    # Testa com texto misturado
    assert is_balanced("func(param1, param2)")
    assert is_balanced("array[index] + dict{key}")
    assert is_balanced("if (condition) { do_something(); }")
    assert not is_balanced("unclosed function(param")
