# ### **1. Tabuada Personalizada**

# Peça ao usuário um número inteiro positivo. Use `for` para exibir a tabuada desse número de 1 a 10.

# **Exemplo:**

# `Digite um número: 7` → exibe 7 x 1 = 7, 7 x 2 = 14, ..., 7 x 10 = 70.

# i = int(input("Digite um numero inteiro: "))

# for c in range(1,11):
#     print(f"{i} x {c} = {i * c}")

# =============================================================
# =============================================================
# =============================================================

# ### **2. Contagem Regressiva com Pausa**

# Peça um número inteiro positivo. Use `while` para fazer uma contagem regressiva até 0,\
#  exibindo cada número. Após o término, exiba `"Fogo!"`.

# numero = int(input("Digite um numero inteiro: "))

# while numero >= 0:
#     print(f"{numero}...")
#     numero -= 1 
# print("Fogo!") 

# =============================================================
# =============================================================
# =============================================================

# ### **3. Média de Notas com `while`**

# Peça notas até que o usuário digite `-1`. Calcule e exiba a média das notas válidas (0 a 10). \
# Ignore entradas inválidas e use `continue` quando necessário.

# nota = []
# i = ""
# while i != "-1":
#     i = input("Digite a nota: ")
#     if 0 <= float(i) <= 10:
#         nota.append(float(i))
#         print(nota)
#     elif i == "-1":
#         break
#     else:
#         continue

# print(f"Sua media foi de: {sum(nota) / len(nota):.2f}")

# =============================================================
# =============================================================
# =============================================================

# ### **4. Validação de Senha com Limite de Tentativas**

# Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar,\
#  exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.

# senha = "senha"
# tent = 3

# while tent > 0:
#     senhadig = input(f"Digite a senha (você tem {tent} tentativas): ")
    
#     if senhadig == senha:
#         print("Acesso liberado!")
#         break
#     else:
#         tent -= 1
#         if tent > 0:
#             print(f"Senha incorreta! Tente novamente.")
        
# if tent == 0:
#     print("Conta bloqueada!")

# =============================================================
# =============================================================
# =============================================================

# ### **5. Números Primos**

# Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.

# num = int(input("Digite um número inteiro: "))

# if num <= 1:
#     print(f"{num} não é primo (números menores ou iguais a 1 não são primos).")
# else:
#     e_primo = True
    
#     for i in range(2, num):
#         if num % i == 0:
#             e_primo = False
#             break
            
#     if e_primo:
#         print(f"O número {num} é primo!")
#     else:
#         print(f"O número {num} não é primo.")

# =============================================================
# =============================================================
# =============================================================

# ### **6. Sequência de Fibonacci**

# Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. \
# Use `for` ou `while` para iterar.


# n = int(input("Quantos termos da sequência de Fibonacci você deseja? "))
# a = 0
# b = 1
# cont = 0

# print("Sequência de Fibonacci:")

# while cont < n:
#     print(a, end=" → " if cont < n - 1 else "")
#     a, b = b, a + b
#     cont += 1

# print("\nFim.")


# =============================================================
# =============================================================
# =============================================================

# ### **7. Soma de Dígitos**

# Peça um número inteiro positivo e calcule a soma de seus dígitos. Use `while` para extrair os dígitos um a um.

# num = int(input("Digite um número inteiro positivo: "))
# soma = 0

# num_orig = num

# while num > 0:
#     digito = num % 10
#     soma += digito
#     num //= 10

# print(f"A soma dos dígitos de {num_orig} é: {soma}")

# =============================================================
# =============================================================
# =============================================================

# ### **8 Menu Interativo**

# Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. As opções podem ser:

# - `1` – Exibir mensagem "Olá!"
# - `2` – Exibir a data/hora atual (use `import datetime`)
# - `3` – Sair

# Use `while True` e `break` para sair.

# import datetime

# while True:
#     print("\n" + "="*20)
#     print("======= MENU =======")
#     print("="*20)
#     print("1 – Exibir 'Olá!'")
#     print("2 – Exibir Data/Hora")
#     print("3 – Sair")
    
#     opcao = input("\nEscolha uma opção: ")

#     if opcao == "1":
#         print("\nOlá! Que bom ver você por aqui.")
    
#     elif opcao == "2":
#         agr = datetime.datetime.now()
#         data_form = agr.strftime("%d/%m/%Y %H:%M:%S")
#         print(f"\nData e Hora atuais: {data_form}")
    
#     elif opcao == "3":
#         print("\nSaindo do sistema... Até logo!")
#         break  

#     else:
#         print("\nOpção inválida! Por favor, digite 1, 2 ou 3.")

# =============================================================
# =============================================================
# =============================================================

# ### **9 Simulador de Lançamento de Dados**

# Simule 100 lançamentos de um dado de 6 faces. Conte quantas vezes cada face foi sorteada \
# e exiba o resultado. Use `for` e `random.randint(1,6)`. (Importe `random`.)

# import random

# contagens = [0] * 7

# for _ in range(100):
#     face = random.randint(1, 6)
#     contagens[face] += 1

# print("-" * 30)
# print("Resultado dos 100 lançamentos:")
# print("-" * 30)
# for face in range(1, 7):
#     print(f"Face {face}: {contagens[face]} vezes")

# =============================================================
# =============================================================
# =============================================================