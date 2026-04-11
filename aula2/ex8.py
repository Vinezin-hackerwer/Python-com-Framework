# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que 
# também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".

ano = int(input('Digite o ano: '))

eh_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
status = ["Ano não bissexto", "Ano bissexto"]

print(status[eh_bissexto])
