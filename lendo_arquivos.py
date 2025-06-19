# Aqui uma forma de dizer é que usamos somente as APIs nativas do python, 
# ou seja, não usamos o pandas sem necessidade
# APIs - São funções onde utilizamos parametros 

import csv

# Caminho para o arquivo CSV
caminho_arquivo: str = 'exemplo.csv'

# Inicializa uma lista vazia para armazenar os dados
arquivo_csv: list = []

# Usa o gerenciador de contexto `with` para abrir o arquivo (ele abre e fecha o arquivo, não tem risco de deixar aberto e não dar pra outra pessoa usar depois)
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    # Cria um objeto leitor de CSV
    leitor_csv = csv.DictReader(arquivo) # Não podia parar aqui, porque nesse momento, ele é um arquivo binário, preciso transformar ele em alguma coisa
    
    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        # Adiciona cada linha (um dicionário) à lista de dados
        arquivo_csv.append(linha)

# Exibe os dados lidos do arquivo CSV
for registro in arquivo_csv:
    print(registro)