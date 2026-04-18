# ### **2. Validação de Triângulo**

# Leia três lados de um triângulo. Verifique se eles formam um triângulo (cada lado é menor que a soma dos outros dois). Se sim, classifique como:

# - `"Equilátero"` (todos os lados iguais)
# - `"Isósceles"` (dois lados iguais)
# - `"Escaleno"` (todos diferentes)

ld1 = float(input("Digite o primeiro lado: "))
ld2 = float(input("Digite o segundo lado: "))
ld3 = float(input("Digite o terceiro lado: "))

if ld1 > ld2 + ld3 or ld2 > ld1 + ld3 or ld3 > ld1 + ld2:
    print("Não é um triangulo")

elif ld1 == ld2 == ld3:
    print("É um equilátero")

elif ld1 == ld2 or ld1 == ld3 or ld2 == ld3:
    print("É um Isósceles")

else:
    print("É um escaleno")
