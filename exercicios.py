# Crie um dicionário para armazenar informações de um livro, 
# incluindo título, autor e ano de publicação. Imprima cada informação.

##01 - Forma de fazer: Um item


# from typing import Dict, Any

# livro_01: Dict[str, Any] = {
#     "Título": "Game of Thrones",
#     "Autor": "George R. R. Martin",
#     "Ano": 1996
# }

# lista_elementos: list = livro_01.items()
# for elemento in lista_elementos:
#     print (elemento)


##02 - Com mais itens

# from typing import Dict, Any

# livro_01: Dict[str, Any] = {
#     "Título": "Game of Thrones",
#     "Autor": "George R. R. Martin",
#     "Ano": 1996
# }

# livro_02: Dict[str, Any] = {
#     "Título": "As Excelências de Cristo",
#     "Autor": "Allen Hood",
#     "Ano": 2019
# }

# lista_livros = []

# lista_livros.append(livro_01)
# lista_livros.append(livro_02)

# print(lista_livros)

##03 - Com mais itens: Posso criar um grande dicionário que terão vários livros
# Não tem certo nem errado em relação a esse ou ao outro
# Mas normalmente quando estamos trabalhando com APIs, usamos esse método pois fica tudo dentro de um pacote só

from typing import Dict, Any

livro_01: Dict[str, Any] = {
    "Título": "Game of Thrones",
    "Autor": "George R. R. Martin",
    "Ano": 1996
}

livro_02: Dict[str, Any] = {
    "Título": "As Excelências de Cristo",
    "Autor": "Allen Hood",
    "Ano": 2019
}

lista_livros = []

lista_livros.append(livro_01)
lista_livros.append(livro_02)

#print(lista_livros)

lista_livros_usando_dict:dict = {
    "livro_01": {"Título": "Game of Thrones",
    "Autor": "George R. R. Martin",
    "Ano": 1996},

    "livro_02": {"Título": "As Excelências de Cristo",
    "Autor": "Allen Hood",
    "Ano": 2019}
}

print(lista_livros_usando_dict["livro_01"]["Título"])