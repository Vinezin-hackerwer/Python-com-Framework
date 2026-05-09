arquivo = open("cadastro.txt", "r")
linhas = arquivo.readlines()
li = 0
for l in linhas:
    print(l.strip())
    # li.append(l)
    li = li + 1


print(li)
arquivo.close()