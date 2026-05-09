# 1. **Criar e escrever** 
#     Crie um programa que peça ao usuário um nome e uma idade, e grave essas informações em um\
#  arquivo chamado `cadastro.txt`, uma pessoa por linha no formato `"nome,idade"`. O programa deve \
# permitir adicionar várias pessoas até que o usuário digite `"sair"`.

with open("cadastro.txt", "a") as arquivo:
    while True:
        nome = input("Digite o nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        idade = input("Digite a idade: ")
        
        arquivo.write(f"{nome},{idade}\n")

print("========================================================")

# # 2. **Ler e exibir** 
# #     Escreva um programa que leia o arquivo `cadastro.txt` criado no exercício anterior e exiba \
# # na tela cada pessoa no formato `"Nome: [nome], Idade: [idade]"`.

try:
    with open("cadastro.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            if len(dados) == 2:
                nome, idade = dados
                print(f"Nome: {nome} | Idade: {idade}")
except FileNotFoundError:
    print("O arquivo cadastro.txt ainda não existe.")

print("========================================================")

# # 3. **Contar linhas**
# #     Crie uma função `contar_linhas(nome_arquivo)` que retorna o número de linhas do arquivo. \
# # Teste com o arquivo `cadastro.txt`.

def contar_linhas(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            return len(linhas)
    except FileNotFoundError:
        return 0

total = contar_linhas("cadastro.txt")
print(f"O arquivo possui {total} linha(s).")

print("========================================================")

# # 4. **Procurar palavra**    
# #     Peça ao usuário uma palavra e um nome de arquivo. Conte quantas vezes essa palavra aparece \
# # no arquivo (ignorando maiúsculas/minúsculas). Exiba o resultado.

palavra_busca = input("Digite a palavra que deseja buscar: ").lower()
nome_arq = input("Digite o nome do arquivo: ")

try:
    with open(nome_arq, "r") as arquivo:
        conteudo = arquivo.read().lower()
        ocorrencias = conteudo.count(palavra_busca)
        print(f"A palavra '{palavra_busca}' aparece {ocorrencias} vezes.")
except FileNotFoundError:
    print("Arquivo não encontrado.")

print("========================================================")

# # 5. **Copiar arquivo**
# #     Peça ao usuário o nome de um arquivo de origem e um arquivo de destino. Copie o conteúdo do \
# # arquivo de origem para o destino, mantendo as linhas.

origem = input("Nome do arquivo de origem: ")
destino = input("Nome do arquivo de destino: ")

try:
    with open(origem, "r") as arq_origem:
        conteudo = arq_origem.read()
    
    with open(destino, "w") as arq_destino:
        arq_destino.write(conteudo)
    
    print(f"Conteúdo copiado de {origem} para {destino} com sucesso!")
except FileNotFoundError:
    print("Arquivo de origem não encontrado.")

print("========================================================")