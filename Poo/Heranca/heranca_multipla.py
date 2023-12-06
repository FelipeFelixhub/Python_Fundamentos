class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)
class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)

class Gato(Mamifero):
    pass

class Orinitorrinco(Mamifero, Ave):
    pass

gato =Gato(nro_patas=4,cor_pelo="amarelo")
print(gato)

ornitorrinco = Orinitorrinco(nro_patas=4, cor_pelo="marrom", cor_bico="laranja")
print(ornitorrinco)