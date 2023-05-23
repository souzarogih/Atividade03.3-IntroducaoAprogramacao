'''Crie uma função chamada "verifica_primo" que receba um número inteiro como parâmetro e
verifique se ele é um número primo. A função deve retornar True se o número for primo e False caso
contrário.'''


def verifica_primo(numero):

    mult = 0
    result = False

    for count in range(2, numero):
        if numero % count == 0:
            mult += 1

    if mult == 0:
        result = True
    else:
        result = False

    return result


print(verifica_primo(10))
