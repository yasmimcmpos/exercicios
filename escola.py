'''
Dado os nomes dos alunos junto com a série em que estão, crie uma lista para a escola.

*Adicione o nome de um aluno à lista de uma nota:
Adicione Jim à 2ª série.OK.

*Obtenha uma lista de todos os alunos matriculados em uma série:
Quais alunos estão na 2ª série?
Nós só temos Jim agora.

*Obtenha uma lista classificada de todos os alunos em todas as séries.
As notas devem ser classificadas como 1, 2, 3, etc.,

*Os alunos dentro de uma série devem ser classificados em ordem alfabética por nome.

========Dúvida: na serie ou na lista que mostra todos?=======


*Quem está matriculado na escola agora?"
Temos Anna, Barb e Charlie na 1ª série,
Alex, Peter e Zoe na 2ª série e Jim na 5ª série.
Então a resposta é: Anna, Barb, Charlie, Alex, Peter, Zoe e Jim.

*Observe que todos os nossos alunos têm apenas um nome,
E cada aluno não pode ser adicionado mais de uma vez a uma série ou à lista.
Se um teste tentar adicionar o mesmo aluno mais de uma vez,
sua implementação deverá indicar que isso está incorreto.

*Os testes para este exercício esperam que sua lista escolar seja implementada
por meio de uma Escola em Python.
Se você não estiver familiarizado com classes em Python, as classes da
documentação do Python são um bom lugar para começar.class
'''


#Quando Usar Classes?
#Quando você precisa modelar objetos do mundo real (ex: Carro, Produto, Usuário).
#Para evitar repetição de código (herança).
#Quando quer organizar funções e dados relacionados em uma única estrutura.


import os
os.system('clear') #Limpa terminal('clear' só para linux n)
from typing_extensions import Dict
class Escola:
    def __init__(self): #metodo contrutor
        self.__aluno_serie__:Dict[str,str] ={}

    def adicionar_aluno(self, nome, serie):
        if serie not in self.__aluno_serie__:
            self.__aluno_serie__[serie] = []

        if nome in self.__aluno_serie__[serie]:
            raise Exception(f"Erro: {nome} já está matriculado na {serie} serie")

        self.__aluno_serie__[serie].append(nome)
        self.__aluno_serie__[serie].sort()  #coloca em ordem
        #return f"{nome} já esta matriculado no curso .."

    def alunos_na_serie(self, serie): #encontra os alunos na serie especifica
        if serie in self.__aluno_serie__:
            return self.__aluno_serie__[serie]
        else:
           raise Exception(f"Não tem alunos")

    def mostra_todos_alunos(self):
        resultado=[] #lista pra por resultado
        for serie in sorted(self.__aluno_serie__.keys()): #sorted serve para colocar na ordem
            resultado.extend(self.__aluno_serie__[serie]) #add final da lista
        return resultado

escola = Escola() # instancia - inicializa um objeto

escola.adicionar_aluno('Anna', 1)
escola.adicionar_aluno('Barb', 1)
escola.adicionar_aluno('Charlie', 1)
escola.adicionar_aluno('Alex', 2)
escola.adicionar_aluno('Peter', 2)
escola.adicionar_aluno('Zoe', 2)
escola.adicionar_aluno('Jim', 5)

print(escola.alunos_na_serie(1))
print(escola.mostra_todos_alunos())
print(escola.adicionar_aluno('Jim', 2)) #'none' de resposta?
print(escola.adicionar_aluno('Jim', 5))