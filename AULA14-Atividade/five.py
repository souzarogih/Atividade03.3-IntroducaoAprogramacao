'''Escreva uma função chamada "encontra_palavras" que receba uma lista de palavras e uma letra como
parâmetros e retorne uma nova lista contendo apenas as palavras que começam com a letra fornecida.'''


def encontra_palavras(lista_de_palavras, letra):
    result = []
    for palavra in lista_de_palavras:
        if letra in palavra:
            result.append(palavra)

    return result


lista = ['teste', 'uniesp', 'database', 'logica', 'introducao', 'brasil']
print('result: ', encontra_palavras(lista, 't'))
