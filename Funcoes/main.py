#Funcoes
def exibir_mensagem():
    print("Olá Mundo")
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")
def exibir_mensagem_3(nome = "Anonimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome = "Felipe")
exibir_mensagem_3()
exibir_mensagem_3("Henrique")

#Retornado valores

def calcular_total(numeros):
    return sum(numeros)
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1

    return antecessor, sucessor

calcular_total([10,20,30])
print(retorna_antecessor_e_sucessor(10))

#Args e Kwargs
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
exibir_poema("Quarta, 15 nov 23","Zen of Python", "Beatiful is better than ugly.", autor="Tim Peters", ano=1999)

#Parametros especiais
#Positional only
def criar_carro(modelo, ano, placa,/,marca,motor,combustivel):
    print(modelo, ano, placa,marca,motor,combustivel)

criar_carro("Ecosporte", 2007, "ABC-1234", marca="Ford", motor="1.6",combustivel="Flex")

#Keyword only
def criar_carro2(*,modelo, ano, placa,marca,motor,combustivel):
    print(modelo, ano, placa,marca,motor,combustivel)

criar_carro2(modelo="Ecosporte", ano=2007, placa="ABC-1234", marca="Ford",motor="1.6",combustivel="Flex")

#Keyword and positional only
def criar_carro3(modelo, ano, placa,/,*,marca,motor,combustivel):
    print(modelo, ano, placa,marca,motor,combustivel)

criar_carro3("Ecosporte", 2007, "ABC-1234", marca="Ford",motor="1.6",combustivel="Flex")