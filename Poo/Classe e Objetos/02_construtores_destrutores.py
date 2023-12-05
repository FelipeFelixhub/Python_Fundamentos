# Construtor __init__
class Cachorro:
    def __int__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

# Destrutor __del__
class Cachorro:
    def __del__(self):
        print("Destruindo a instancia!!")
c = Cachorro()
del c