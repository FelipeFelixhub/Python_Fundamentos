# Tuplas
frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil")

# Acesso direto
frutas[0]
frutas[2]

# Acesso negativo
frutas[-1]
frutas[-3]

# Tuplas aninhadas
matriz = [
    [1, "a", 2]    ,
    ["b", 3, 4],
    [6,5,"c"]
    ]

matriz[0]
matriz[0][0]
matriz[0][-1]
matriz[-1][-1]

# Metodos de uma tupla
# ().count
cores = ("vermelho", "azul", "verde", "azul",)
cores.count("vermelho")
cores.count("azul")
cores.count("verde")

#().index
linguagens = ("python", "js", "c", "java", "csharp",)
linguagens.index("java")
linguagens.index("python")

#.()len
len(linguagens)