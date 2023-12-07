class Estudante:
    escola = "DIO"
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula= matricula
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
def mostrar_valores(*objs):
        for obj in objs:
            print(obj)

aluno_1 = Estudante("Felipe", 1)
aluno_2 = Estudante("Henrique", 2)
print(aluno_1)
print(aluno_2)

Estudante.escola = "Fatec"
aluno_3 = Estudante("Carol", 3)


mostrar_valores(aluno_1, aluno_2, aluno_3)
