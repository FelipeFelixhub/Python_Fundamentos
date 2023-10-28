from builtins import print

# Manipulando String

curso = "pYtHoN"

print(curso.upper())
print(curso.lower())
print(curso.title())

#Eliminando espaços em branco
texto = "    Snake "

print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())

# Juncoes e centralizacao
text2 = "Cobra"

print(text2.center(10, "#"))
print(".".join(text2))

# Interpolacao de string - f-string
nome1 = "Felipe"
idade = 20
profissao = "Analista de dados"
linguagem = "Python"

print(f"Olá, me chamo {nome1}. Tenho {idade} anos, trabalho como {profissao} e atualmente estudo {linguagem}")

# Formatar string com f-string
PI = 3.141596

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

# Fatiamento de String
nome2 = "Felipe Douglas dos Santos Felix"

print(nome2[0])
print(nome2[:7])
print(nome2[:14])
print(nome2[14:15])
print(nome2[14:15:2])
print(nome2[:])
print(nome2[:: -1])

# String Múltiplas linhas

nome = "Felipe"

mensagem = f'''
        Olá meu nmome é {nome},
        Eu estou aprendendo Python '''

print(mensagem)

print(
        """
        ===== MENU =====
        1 - Depositar
        2 - Sacar
        3 - Sair
        
        ================
"""
)
