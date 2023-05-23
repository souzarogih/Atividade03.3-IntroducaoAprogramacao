'''Escreva uma função chamada "conta_vogais" que receba uma string como parâmetro e retorne o
número de vogais presentes nessa string. Considere que a string pode conter letras maiúsculas e
minúsculas.'''


def conta_vogais(palavra):
    vogais = 'aeiouAEIO'
    count = 0
    for char in palavra:
        if char in vogais:
            count += 1
    return count

print("Quantidade de vogais", conta_vogais("teste"))
