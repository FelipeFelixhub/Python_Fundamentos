
#VETORES
N: int
N = int(input("Quantos numeros voce vai digitar? "))
vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Digite um numero: "))

print()
print("NUMEROS DIGITADOS: ")
for i in range(0, N):
    print(f"{vet[i]:.1f}")

#MATRIZES
A: int
B: int

A = int(input("Quantas linhas vai ter a matriz? "))
B = int(input("Quantas colunas vai ter a matriz? "))

mat: [[int]] = [[0 for x in range(B)] for x in range(A)]

for i in  range(0, A):
    for j in  range(0, B):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))
print()
print("MATRIZ DIGITADA: ")
for i in range(0, A):
    for j in range(0, B):
        print(f"{mat[i][j]} ", end="")
    print()