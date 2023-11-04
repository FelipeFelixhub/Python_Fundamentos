# Listas

frutas = ["laranja", "manga", "melancia"]

verduras = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "Sao Paulo", True]

print(frutas)
print(verduras)
print(letras)
print(numeros)
print(carro)

# Acessando elementos da lista
print(frutas[0])
print(frutas[2])

# Listas aninhadas
matriz = [
    [1, "a", 2]    ,
    ["b", 3, 4],
    [6,5,"c"]
    ]

matriz[0]
matriz[0][0]
matriz[0][-1]
matriz[-1][-1]

# [].append
lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

# [].clear
lista = [1, "Python", [40, 30, 20]]
print(lista)

lista.clear()

print(lista)

# [].copy
lista = [1, "Python", [40, 30, 20]]

lista.copy()
print(lista)

# [].count
cores = ["vermelho", "azul", "verde", "azul"]
print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

# [].extend
linguagens = ["Python", "js", "c"]
print(linguagens)
linguagens.extend(["java", "csharp"])
print(linguagens)

# [].index
linguagens = ["Python", "js", "c", "java", "csharp", "java"]
print(linguagens.index("java"))
print(linguagens.index("Python"))

# [].pop
linguagens = ["Python", "js", "c", "java", "csharp", "java"]
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))

# [].remove
linguagens = ["Python", "js", "c", "java", "csharp", "java"]
linguagens.remove("c")
print(linguagens)

# []. reverse
linguagens = ["Python", "js", "c", "java", "csharp", "java"]
linguagens.reverse()
print(linguagens)

# [].sort
linguagens = ["python", "js", "c", "java", "csharp", "java"]
linguagens.sort()
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp", "java"]
linguagens.sort(reverse=True)
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp", "java"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp", "java"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

# [].len
linguagens = ["python", "js", "c", "java", "csharp", "java"]
print(len(linguagens))

# [].sorted
linguagens = ["python", "js", "c", "java", "csharp", "java"]

print(sorted(linguagens, key=lambda x: len(x)))


print(sorted(linguagens, key=lambda x: len(x), reverse=True))