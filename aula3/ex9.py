# ### **9. Validação de Data**

# Leia um dia (1-31), mês (1-12) e ano (qualquer). Verifique se a data é válida, considerando meses com 30/31 dias e fevereiro (28 ou 29 dias, \
# considerando ano bissexto: divisível por 400 ou (divisível por 4 e não por 100)).

meses   =  [0,1,2,3,4,5,6,7,8,9,10,11,12]
dias_meses = [0,list(range(0,31)),
              list(range(0,29)),
              list(range(0,31)),
              list(range(0,30)),
              list(range(0,31)),
              list(range(0,30)),
              list(range(0,31)),
              list(range(0,31)),
              list(range(0,30)),
              list(range(0,31)),
              list(range(0,30)),
              list(range(0,31))
              ]

ano =  int(input('ano: '))
mes =  int(input('Digite o número do mês: '))
dia =  int(input('Digite o dia:  '))


if (ano % 400 == 0 or ano % 4 == 0) or (ano % 100 ==0):
    print('ano bissexto...')
else:
    print('Não é bissexto...')

if mes in meses:
    i =  meses.index(mes)
    if dia in dias_meses[i]:
        print('data válida')
else:
    print('Data invalida')
    