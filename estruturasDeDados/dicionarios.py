# Dicionarios
from _operator import contains

pessoa = {"nome": "Felipe", "idade": 31} #forma mais comum

pessoa = dict(nome = "Felipe", idade = 31)

pessoa["telefone"] = "1234-5678"

# Acesso aos dados
dados = {"nome": "Felipe", "idade": 31, "telefone": "4455-1234"}

dados["nome"]
dados["idade"]
dados["telefone"]
print(dados["nome"])

dados["nome"] = "Henrique"
print(dados["nome"])

# Dicionario aninhado
contatos = {
    "felipe@email.com":{"nome":"Felipe","telefone":"2345-5678"},
    "henrique@email.com":{"nome":"Henrique","telefone":"2345-5699"},
    "carol@email.com":{"nome":"Caroline","telefone":"2345-5600"}
}
print(contatos)
print(contatos["felipe@email.com"]["telefone"])

# Iterar dicionario
for chave in contatos:
    print(chave,contatos[chave])

# melhor forma
for chave, valor in contatos.items():
    print(chave, valor)

# Metodos da classe dict
# clear
contatos = {
    "felipe@email.com":{"nome":"Felipe","telefone":"2345-5678"},
    "henrique@email.com":{"nome":"Henrique","telefone":"2345-5699"},
    "carol@email.com":{"nome":"Caroline","telefone":"2345-5600"}
}
contatos.clear()
print(contatos)

# Copy
contatos = {
    "felipe@email.com":{"nome":"Felipe","telefone":"2345-5678"}
}
copia = contatos.copy()
copia["felipe@email.com"] = {"nome":"Fe"}

print(contatos["felipe@email.com"])
print(copia["felipe@email.com"])

#fromkeys - adiciona varias chaves de uma vez
dic = dict.fromkeys(["nome","telefone"])

dict.fromkeys(["nome","telefone"], "vazio")

#get
contatos = {
    "felipe@email.com":{"nome":"Felipe","telefone":"2345-5678"}
}
# contatos["chave"] erro

contatos.get("chave")
contatos.get("chave",{})
contatos.get("felipe@email.com",{})

#items
contatos = {
    "felipe@email.com":{"nome":"Felipe","telefone":"2345-5678"}
    }
contatos.items()

#keys - retorna as chaves
contatos = {
    "felipe@email.com": {"nome": "Felipe", "telefone": "2345-5678"}
}
print(contatos.keys())

#pop
contatos = {
    "felipe@email.com": {"nome": "Felipe", "telefone": "2345-5678"}
}
contatos.pop("felipe@email.com")
contatos.pop("henrique@email.com", {})

#popitem - remove na ordem

contatos = {
    "felipe@email.com": {"nome": "Felipe", "telefone": "2345-5678"}
}
contatos.popitem()

#setdefault

#update
contatos = {
    "felipe@email.com": {"nome": "Felipe", "telefone": "2345-5678"}
}
contatos.update({"felipe@email.com": {"nome": "Fe"}})
contatos.update({"henrique@email.com": {"nome": "Henriquinho"}})
print(contatos)

#Values
contatos = {
    "felipe@email.com":{"nome":"Felipe","telefone":"2345-5678"},
    "henrique@email.com":{"nome":"Henrique","telefone":"2345-5699"},
    "carol@email.com":{"nome":"Caroline","telefone":"2345-5600"}
}
print(contatos.values())

#in
contatos = {
    "felipe@email.com":{"nome":"Felipe","telefone":"2345-5678"},
    "henrique@email.com":{"nome":"Henrique","telefone":"2345-5699"},
    "carol@email.com":{"nome":"Caroline","telefone":"2345-5600"}
}
"felipe@email.com" in contatos #True
"valentina@gmail.com" in contatos #False
"idade" in contatos["felipe@email.com"] #False

#del
contatos = {
    "felipe@email.com":{"nome":"Felipe","telefone":"2345-5678"},
    "henrique@email.com":{"nome":"Henrique","telefone":"2345-5699"},
    "carol@email.com":{"nome":"Caroline","telefone":"2345-5600"}
}
del contatos["felipe@email.com"]["telefone"]
del contatos["carol@email.com"]
