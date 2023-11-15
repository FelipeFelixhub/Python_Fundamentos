# Dicionarios
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