import statistics as sta


def media_homens(lista_medias):
    return sta.mean(lista_medias)

qtd_total = 0
data = []
user = 1

qtd_mulheres = 0
maior_altura = 0
menor_altura = 0
dados_media_homens = []

while qtd_total <= 14:
    altura = float(input('Digite a altura: '))
    genero = input('Digite o genero: ')

    data.append({'user': user, 'altura': altura, 'genero': genero})

    if genero == 'f' or genero == 'F':
        qtd_mulheres += 1

    if genero == 'm' or genero == 'M':
        dados_media_homens.append(altura)

    if altura > maior_altura and menor_altura == 0:
        maior_altura = altura
        menor_altura = altura

    elif altura > maior_altura:
        maior_altura = altura

    elif altura < menor_altura:
        menor_altura = altura

    user += 1
    qtd_total += 1

print(data)
print(f'Quantidade de mulheres {qtd_mulheres}')
print(f'Maior altura: {maior_altura} e menor altura: {menor_altura}')
print(f'Media das alturas dos homens: {media_homens(dados_media_homens)}')

