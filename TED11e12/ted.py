import csv

# Nossa fábrica de software ficou especializada em trabalhar com arquivos. Desta maneira, nos foi enviado um arquivo
# CSV para leitura e verificação de um dado. Os clientes desejam saber qual o filme com maior público no ano de exibição.
# 2009 - 2019

with open('filmes.csv', 'r', encoding='utf-8') as f:
    maior_publico = {
        2019: 0,
        2018: 0,
        2017: 0,
        2016: 0,
        2015: 0,
        2014: 0,
        2013: 0,
        2012: 0,
        2011: 0,
        2010: 0,
        2009: 0,
    }
    reader = csv.reader(f, delimiter=',')
    for i, linha in enumerate(reader):
        if i == 0:
            pass
        else:
            campo1 = int(linha[1])
            campo8 = float(linha[8])
            print(f'Ano: {campo1}')
            print(f'Público atual: {campo8}')
            if campo1 == 2019:
                if campo8 > maior_publico[2019]:
                    maior_publico[2019] = campo8
                else:
                    pass
            if campo1 == 2018:
                if campo8 > maior_publico[2018]:
                    maior_publico[2018] = campo8
                else:
                    pass
            if campo1 == 2017:
                if campo8 > maior_publico[2017]:
                    maior_publico[2017] = campo8
                else:
                    pass
            if campo1 == 2016:
                if campo8 > maior_publico[2016]:
                    maior_publico[2016] = campo8
                else:
                    pass
            if campo1 == 2015:
                if campo8 > maior_publico[2015]:
                    maior_publico[2015] = campo8
                else:
                    pass
            if campo1 == 2014:
                if campo8 > maior_publico[2014]:
                    maior_publico[2014] = campo8
                else:
                    pass
            if campo1 == 2013:
                if campo8 > maior_publico[2013]:
                    maior_publico[2013] = campo8
                else:
                    pass
            if campo1 == 2012:
                if campo8 > maior_publico[2012]:
                    maior_publico[2012] = campo8
                else:
                    pass
            if campo1 == 2011:
                if campo8 > maior_publico[2011]:
                    maior_publico[2011] = campo8
                else:
                    pass
            if campo1 == 2010:
                if campo8 > maior_publico[2010]:
                    maior_publico[2010] = campo8
                else:
                    pass
            if campo1 == 2009:
                if campo8 > maior_publico[2009]:
                    maior_publico[2009] = campo8
                else:
                    pass
        print('Maior público em 2019', maior_publico[2019])
        print('Maior público em 2018', maior_publico[2018])
        print('Maior público em 2017', maior_publico[2017])
        print('Maior público em 2016', maior_publico[2016])
        print('Maior público em 2015', maior_publico[2015])
        print('Maior público em 2014', maior_publico[2014])
        print('Maior público em 2013', maior_publico[2013])
        print('Maior público em 2012', maior_publico[2012])
        print('Maior público em 2011', maior_publico[2011])
        print('Maior público em 2010', maior_publico[2010])
        print('Maior público em 2009', maior_publico[2009])
        print('\n')



