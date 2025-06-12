import pytest
from pytest import raises

from exercicios.ex2 import Escola

##Comentar com Fazenda:
# Pytest não queria importar então eu troquei para "with pytest.raises()...


def test_de_adicionar_um_aluno() -> None:
    escola = Escola()
    serie = 1
    escola.adicionar_aluno("Anna", serie)

    assert "Anna" in escola.alunos_na_serie(serie)
    with pytest.raises(Exception, match="Aluno já está matriculado"):
        escola.adicionar_aluno("Anna", 1)


def test_erro_nao_tem_aluno() -> None:
    escola = Escola()
    escola.adicionar_aluno("Anna", 1)

    with raises(Exception, match="Não tem alunos"):
        escola.alunos_na_serie(2)


def test_conferir_se_mostra_todos() -> None:
    escola = Escola()
    escola.__aluno_serie__ = {1: ["Barb", "Charlie"], 5: ["Jim"]}

    resultado = escola.mostra_todos_alunos()
    esperado = ["Barb", "Charlie", "Jim"]
    assert resultado == esperado


# def test_erro_aluno_ja_existe() -> None:
# escola = Escola()
# escola.adicionar_aluno("Anna", 1)

# with raises(Exception, match="Aluno já está matriculado"):
# escola.adicionar_aluno("Anna", 1)


# escola.adicionar_aluno("Barb", 1)
# escola.adicionar_aluno("Charlie", 1)
# escola.adicionar_aluno("Alex", 2)
# escola.adicionar_aluno("Peter", 2)
# escola.adicionar_aluno("Zoe", 2)
# escola.adicionar_aluno("Jim", 5)

# print(escola.alunos_na_serie(2))
# print(escola.mostra_todos_alunos())
