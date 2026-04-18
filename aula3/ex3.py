# ### **3. Cálculo de IMC com Faixas**

# Leia peso (kg) e altura (m). Calcule o IMC e classifique conforme a tabela da OMS:

# - `"Abaixo do peso"` se IMC < 18.5
# - `"Peso normal"` se 18.5 ≤ IMC < 25
# - `"Sobrepeso"` se 25 ≤ IMC < 30
# - `"Obesidade"` se IMC ≥ 30


peso = float(input("Digite o seu peso: "))
alt = float(input("Digite a sua altura: "))
imc = peso / (alt ** 2)

if imc < 18.5:
    print("Seu imc de " , imc, "é Abaixo do peso")

elif imc >= 18.5 and imc < 25:
    print("Seu imc de ", imc, "é Peso normal")

elif imc >= 25 and imc < 30:
    print("Seu imc de ", imc, "é Sobrepeso")

elif imc >= 30:
    print("Seu imc de ", imc, "é Obesidade")