# ### **4. Imposto de Renda Simplificado**

# Leia o salário bruto mensal e calcule o desconto do INSS (11% sobre o salário, limitado a R$ 1.500,00) e o IRRF conforme tabela:

# - Isento se salário bruto ≤ R$ 2.500,00
# - 7,5% sobre o que exceder R$ 2.500,00 até R$ 3.500,00
# - 15% sobre o que exceder R$ 3.500,00 até R$ 5.000,00
# - 27,5% sobre o que exceder R$ 5.000,00
    
#     Exiba o salário líquido após os descontos.

salBrut = float(input("Digite o seu salário: "))

inss = salBrut * 0.11
if inss > 1500:
    inss = 1500

irrf = 0

salTot = salBrut - inss


if salBrut <= 2500:
    print("Seu salário liquido é de: " , salTot)

elif salBrut > 2500 and salBrut <= 3500:
    print("Seu salário liquido é de: " , salTot - (salBrut * 0.075))

elif salBrut > 3500 and salBrut <= 5000:
    print("Seu salário liquido é de: " , salTot - (salBrut * 0.15))

elif salBrut > 5000:
    print("Seu salário liquido é de: " , salTot - (salBrut * 0.275))