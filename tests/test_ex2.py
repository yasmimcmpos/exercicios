from pytest import raises

from exercicios.ex2 import Escola


def test_de_adicionar_um_aluno() -> None:
    escola = Escola()
    serie = 1
    escola.adicionar_aluno("Anna", serie)

    assert "Anna" in escola.alunos_na_serie(serie)


def test_erro_nao_tem_aluno() -> None:
    escola = Escola()
    escola.adicionar_aluno("Anna", 1)

    with raises(Exception, match="Não tem alunos"):
        escola.alunos_na_serie(2)


# escola.adicionar_aluno("Barb", 1)
# escola.adicionar_aluno("Charlie", 1)
# escola.adicionar_aluno("Alex", 2)
# escola.adicionar_aluno("Peter", 2)
# escola.adicionar_aluno("Zoe", 2)
# escola.adicionar_aluno("Jim", 5)

# print(escola.alunos_na_serie(2))
# print(escola.mostra_todos_alunos())
