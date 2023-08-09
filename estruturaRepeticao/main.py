
# WHILE
x: int
soma = 0
x = int(input("Digite o primeiro numero: "))

while x != 0:
    soma = soma + x
    x = int(input("Digite outro numero: "))
print(f"SOMA:  {soma}")

#FOR
y: int
N = int(input("Quantos numeros serao digitados? "))

soma2 = 0
for i in range(0, N):
    y = int(input("Digite um numero: "))
    soma2 = soma2 + y
print(f"SOMA: {soma2}")