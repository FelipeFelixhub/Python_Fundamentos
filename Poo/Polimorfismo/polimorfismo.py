class Passaro:
    def voar(self):pass
class Pardarl(Passaro):
    def voar(self):
        print("Pardal voa!")
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa!")

def plano_de_voo(passaro):
    passaro.voar()

plano_de_voo(Pardarl())
plano_de_voo(Avestruz())