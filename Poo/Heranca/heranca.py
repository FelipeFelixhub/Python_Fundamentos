class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def ligar_motor(self):
            print("ligando motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass
class Caminhao(Veiculo):
    def __init__(self,cor, placa, numero_rodas, carregado):
        super().__init__( cor, placa, numero_rodas)
        self.carregado = carregado
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "fdh-2017", 2)
moto.ligar_motor()

carro = Carro("preto", "ggg-1234", 4)
carro.ligar_motor()

caminhao = Caminhao("branco", "scn-0000", 16, True)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(moto.cor, moto.placa, moto.numero_rodas)