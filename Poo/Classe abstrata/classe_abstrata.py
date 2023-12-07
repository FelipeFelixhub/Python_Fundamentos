from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
    def desligar(self):
        print("Desligando a TV")

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar")

    def desligar(self):
            print("Desligando o Ar")


controle_tv = ControleTV()
controle_tv.ligar()
controle_tv.desligar()

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()