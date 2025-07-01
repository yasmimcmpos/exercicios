from pytest import raises

from exercicios.ex2 import Escola


def test_de_adicionar_um_aluno() -> None:
    escola = Escola()
    serie = 1
    escola.adicionar_aluno("Anna", serie)

    assert "Anna" in escola.alunos_na_serie(serie)

    with raises(Exception, match="Aluno já está matriculado"):
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
