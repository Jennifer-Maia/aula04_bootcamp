# Para saber tudo que posso fazer com as listas pesquisar: list pyton doc methods
# (Sempre usa [])
#Append é para adicionar um item
produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

produtos: list = []

produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)

#produtos.pop() #Remove o último item, possar várias vezes
#produtos.remove() #Remove o item que eu colocar mas é menos performático

print(produtos)

#Extend é para adicionar um range 
numeros = []
numeros.extend(range(0,5))
print(numeros)