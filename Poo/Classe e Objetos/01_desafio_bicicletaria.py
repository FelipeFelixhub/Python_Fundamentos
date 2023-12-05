
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzinar(self):
        print("Plim Plim")
    def parar(self):
        print("Parando a bicicleta")
        print("Bicicleta parada!")
    def correr(self):
        print("Acelerando a bicicleta")

    def __str__(self):
        return    f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
b1 = Bicicleta("vermelha", "caloi", 2022, 600)

b1.buzinar()
Bicicleta.buzinar(b1)
b1.parar()
b1.correr()

print(b1.cor, b1.valor, b1.modelo)

print(b1)

