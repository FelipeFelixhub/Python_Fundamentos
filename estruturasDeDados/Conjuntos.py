# Set
numeros = set([1, 2, 3, 1, 2, 3, 4])
print(numeros)

fruta = set("abacaxi")
print(fruta)

linguagens = {"python", "java", "python"}
print(linguagens)

carros = set(("palio", "gol", "celta", "palio"))
print(carros)

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Metodos da classe Set
#{}.union
conjunto_a = {1,2}
conjunto_b = {3,4}

uniao = conjunto_a.union(conjunto_b)
print(uniao)

#{}.intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

intersec = conjunto_a.intersection(conjunto_b)
print(intersec)

#{}.difererence
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

dif1 = conjunto_a.difference(conjunto_b)
dif2 = conjunto_b.difference(conjunto_a)
print(dif1)
print(dif2)

#{}. symmetric_diference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

simetrico = conjunto_a.symmetric_difference(conjunto_b)
print(simetrico)

#{}.issubset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

sub1 =conjunto_a.issubset(conjunto_b)
sub2 = conjunto_b.issubset(conjunto_a)
print(sub1)
print(sub2)

#{}.issuperset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

super1 = conjunto_a.issuperset(conjunto_b)
super2 = conjunto_b.issuperset(conjunto_a)
print(super1)
print(super2)

#{}.isdisjoint
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b)
conjunto_a.isdisjoint(conjunto_c)

#{}.add
sorteio = {1, 23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)

#{}.clear
sorteio = {1, 23}
sorteio.clear()
print(sorteio)

#{}.copy
sorteio = {1, 23}
sorteio2 = sorteio.copy()
print(sorteio2)

#{}.discard
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,9,0}

numeros.discard(1)
numeros.discard(45)

print(numeros)

#{}.pop
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,9,0}
print(numeros)
numeros.pop()
numeros.pop()

print(numeros)

#{}.remove
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,9,0}
numeros.remove(0)
print(numeros)

#Len
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,9,0}
len(numeros)

#in
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,9,0}
1 in numeros
10 in numeros
