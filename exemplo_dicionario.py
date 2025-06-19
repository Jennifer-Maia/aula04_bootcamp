# CHAVE - VALOR (Sempre usa {})
# é no estilo json
# Quando jogamos um excel para o python, ele vira um json!
# Para saber tudo que posso fazer com dict pesquisar: methods dict in python (w3school)

# prod_01: dict = {
#     "nome": "Sapato",
#     "quantidade": 39,
#     "preco": 10.38,
#     "disponibilidade": True
# }

# prod_02: dict = {
#     "nome": "Televisão",
#     "quantidade": 0,
#     "preco": 975.50,
#     "disponibilidade": False
# }

# carrinho: list = []

# carrinho.append(prod_01)
# carrinho.append(prod_02)

# print(carrinho) #Aqui tenho um lista de dicionários


## Transformando dicionário em json
# Não podemos falar que json (JS) é o dicionário do python, 
# eles tem algumas pequenas diferenças que se 
# não tratadas vão gerar anomalias em um banco de dados depois por exemplo

import json

prod_01: dict = {
    "nome": "Sapato",
    "quantidade": 39,
    "preco": 10.38,
    "disponibilidade": True
}

prod_02: dict = {
    "nome": "Televisão",
    "quantidade": 0,
    "preco": 975.50,
    "disponibilidade": False
}

carrinho: list = []

carrinho.append(prod_01)
carrinho.append(prod_02)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)
