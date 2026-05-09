# # Abre o arquivo para escrita (cria/substitui)
# arquivo = open("dados.txt", "w")
# arquivo.write("Linha 1\n")
# arquivo.write("Linha 2\n")
# arquivo.close()


# x  = open('arquivo.txt','w')
# x.write('fhsjkdfhjksdhfjkshdjkfhjsdhfjshdfjkhsjdfksd\n')
# x.close()


# x = open('arquivo.txt', 'a')
# x.write('adiocione....')
# x.close()

print("========================================================")

# 1
arquivo = open('cadastro.csv', 'r')
for linha in arquivo:
    dados = linha.strip().split(',')
    nome =  dados[0]
    idade = dados[1]
    venda = dados[2]
    print('Nome', nome, 'idade', idade, 'vendas', venda)

arquivo.close()

print("========================================================")

# 2
with open('cadastro.csv', 'r') as c:
    conteudo = c.read()
    print(conteudo)

print("========================================================")