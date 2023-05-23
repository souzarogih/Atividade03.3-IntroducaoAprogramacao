'''Escreva uma função chamada "converte_tempo" que receba um valor inteiro representando um tempo
em segundos e retorne uma string formatada como "horas:minutos:segundos".'''


def converte_tempo(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d:%02d" % (hour, minutes, seconds)

print(converte_tempo(15956))
