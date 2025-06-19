## Utilizamos função para empacotar coisas - como engenheiros de dados, criamos para outras pessoas utilizarem
## Ordenação de Lista: Não usamos dessa forma pois já existe a função .sort()
## Função servem para não precisarmos repetirmos a mesma coisa duas vezes, 
# depois chamamos ela usando por exemplo: "from exemplo_funcao import ordernar_lista_numeros"

lista_numeros: list = [40,50,60,70,0,-408593,1,50]
lista_numeros_02: list = [40,60,70,0,-408593,1,50]
lista_numeros_03: list = [40,60,70,0,1,50]

def ordernar_lista_numeros(numeros: list) -> list:
    nova_lista_numeros = numeros.copy()

    for i in range(len(nova_lista_numeros)):
        for j in range(i+1, len(nova_lista_numeros)):
            if nova_lista_numeros[i] > nova_lista_numeros [j]:
                nova_lista_numeros[i], nova_lista_numeros [j] = nova_lista_numeros[j], nova_lista_numeros [i]

    return nova_lista_numeros

nova_lista = ordernar_lista_numeros(lista_numeros)
nova_lista_2 = ordernar_lista_numeros(lista_numeros_02)
nova_lista_3 = ordernar_lista_numeros(lista_numeros_03)

print(nova_lista_2)



