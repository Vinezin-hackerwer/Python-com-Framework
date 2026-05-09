# 4


nome_arquivo =  input('Nome do arquivo: ')
palavra =  input('Palavra: ')


# arquivo = open(nome_arquivo, 'w')
# arquivo = open(nome_arquivo, 'a')
# arquivo.write(palavra)


arquivo = open(nome_arquivo,'r')
contador  =  0


for linha in arquivo:
    linha  =  linha.lower()
    contador =  contador + linha.count(palavra.lower())


arquivo.close()


print('contador da palavra', contador)



# n =  'teste'


# print(n.count('s'))

