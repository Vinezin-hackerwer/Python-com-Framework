# ### **1. Classificação de Notas com Menção**

# Crie um programa que leia a nota de um aluno (0 a 10) e exiba a menção correspondente:

# - `"Excelente"` se nota >= 9
# - `"Bom"` se nota >= 7 e < 9
# - `"Regular"` se nota >= 5 e < 7
# - `"Insuficiente"` se nota < 5

nota = float(input("Digite sua nota: "))
if nota >= 9:
    print("Excelente")
elif nota < 9 and nota >= 7:
    print("Bom")
elif nota < 7 and nota >= 5:
    print("Regular")
else:
    print("Insuficiente")
