# ### **1. Calculadora com Funções**

# Crie funções separadas para as quatro operações básicas (`somar`, `subtrair`, `multiplicar`, `dividir`).\
#  Em seguida, escreva um programa que leia dois números e a operação desejada (como string) e chame a função correspondente. \
# A divisão deve tratar divisão por zero.

# def somar(a, b):
#     return a + b

# def subtrair(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     if b == 0:
#         return "Erro: Divisão por zero não permitida!"
#     return a / b

# n1 = float(input("Digite o primeiro número: "))
# n2 = float(input("Digite o segundo número: "))

# print("\nOperações disponíveis: +, -, *, /")
# operacao = input("Qual operação deseja realizar? ")

# if operacao == "+":
#     resultado = somar(n1, n2)
# elif operacao == "-":
#     resultado = subtrair(n1, n2)
# elif operacao == "*":
#     resultado = multiplicar(n1, n2)
# elif operacao == "/":
#     resultado = dividir(n1, n2)
# else:
#     resultado = "Operação inválida!"

# print(f"\nResultado: {resultado}")

# =============================================================
# =============================================================
# =============================================================

# ### **2. Validador de CPF (simplificado)**

# Crie uma função `validar_cpf(cpf)` que recebe uma string com 11 dígitos e retorna `True` se for válido \
# (use o algoritmo básico de validação de CPF). Em seguida, teste a função com alguns CPFs.

# https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/

# def validar_cpf(cpf):
#     cpf = "".join(filter(str.isdigit, cpf))

#     if len(cpf) != 11 or cpf == cpf[0] * 11:
#         return False

#     soma = 0
#     for i in range(9):
#         soma += int(cpf[i]) * (10 - i)
    
#     resto = soma % 11
#     digito1 = 0 if resto < 2 else 11 - resto

#     soma = 0
#     for i in range(10):
#         soma += int(cpf[i]) * (11 - i)
    
#     resto = soma % 11
#     digito2 = 0 if resto < 2 else 11 - resto

#     return int(cpf[9]) == digito1 and int(cpf[10]) == digito2

# while True:
#     print("\n" + "-"*30)
#     entrada = input("Digite o CPF para validar (ou 'sair'): ")

#     if entrada.lower() == 'sair':
#         print("Encerrando validador...")
#         break

#     if validar_cpf(entrada):
#         print(f"O CPF {entrada} é VÁLIDO.")
#     else:
#         print(f"O CPF {entrada} é INVÁLIDO.")

# =============================================================
# =============================================================
# =============================================================

# ### **3. Gerador de Tabuada**

# Escreva uma função `tabuada(numero, inicio=1, fim=10)` que exibe a tabuada do `numero` no intervalo `[inicio, fim]`.\
#  Se os argumentos `inicio` e `fim` não forem fornecidos, use 1 e 10.



# =============================================================
# =============================================================
# =============================================================

# ### **4. Contador de Palavras**

# Crie uma função `contar_palavras(texto)` que retorna um dicionário com a contagem de cada palavra no texto \
# (considere palavras separadas por espaços). O programa principal deve ler uma frase e exibir o resultado.

# =============================================================
# =============================================================
# =============================================================

# ### **5. Ordenação Personalizada**

# Implemente uma função `ordenar_lista(lista, crescente=True)` que retorna uma nova lista ordenada. Se `crescente=True`, \
# ordena em ordem crescente; caso contrário, decrescente. Não use `sorted()` ou `list.sort()` \
# (implemente o algoritmo de ordenação de sua escolha, como bolha).

# =============================================================
# =============================================================
# =============================================================

# ### **6. Jogo de Adivinhação**

# Crie uma função `jogar()` que sorteia um número entre 1 e 100 e dá dicas ("maior", "menor") até o usuário acertar. \
# Use `random.randint()`. A função deve retornar o número de tentativas. No programa principal, chame a função e exiba \
#  quantas tentativas foram necessárias.

# =============================================================
# =============================================================
# =============================================================

# ### **7. Conversor de Bases**

# Escreva uma função `converter_base(numero, base_origem, base_destino)` que converte um número entre bases 2, 8, 10 e 16.\
#  A entrada `numero` é uma string. A função retorna a string convertida. (Exemplo: `converter_base("1010", 2, 16)` → `"A"`). \
# Use `int()` com base e depois formate.

# Conteúdo para auxiliar

# https://dev.to/udanielnogueira/valores-em-binario-octal-e-hexadecimal-em-python-pn7

# =============================================================
# =============================================================
# =============================================================

# ### **8. Sistema de Caixa Eletrônico**

# Crie uma função `sacar(valor)` que retorna um dicionário com a quantidade de notas de 100, 50, 20, 10, 5 e 2 necessárias \
# para o valor. O valor deve ser inteiro e positivo. Caso não seja possível (valor não múltiplo de 2), a função retorna `None`. No programa \
# principal, chame a função e exiba o resultado.

# =============================================================
# =============================================================
# =============================================================

# ### **9. Análise de Lista com Múltiplos Retornos**

# Escreva uma função `analisar_lista(lista)` que retorna quatro valores: o menor valor, o maior valor, a soma e a média. No programa \
# principal, receba uma lista de números do usuário (terminada por -1) e exiba os resultados usando desempacotamento.

# =============================================================
# =============================================================
# =============================================================

# ### **10. Função que Modifica Lista Global**

# Crie uma lista global `estoque = []`. Escreva funções:

# - `adicionar_produto(nome, quantidade)`: adiciona um dicionário `{"nome": nome, "quantidade": quantidade}` à lista global.
# - `remover_produto(nome)`: remove o produto com esse nome (se existir).
# - `listar_estoque()`: exibe todos os produtos.
    
#     Use a palavra-chave `global` para modificar a lista dentro das funções. O programa principal deve apresentar um menu \
# interativo para o usuário.


# =============================================================
# =============================================================
# =============================================================
