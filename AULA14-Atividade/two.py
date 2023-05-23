'''Crie uma função chamada "calcula_fatorial" que receba um número inteiro como parâmetro e retorne
o seu fatorial. O fatorial de um número é o produto de todos os números inteiros de 1 até o próprio
número.'''


def calcula_fatorial(numero):

    resultado=1
    count=1

    while count <= numero:
        resultado *= count
        count += 1

    return resultado


print(calcula_fatorial(3))
