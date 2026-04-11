# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba 
# "Peso normal" ou "Fora da faixa".

peso = float(input('peso: '))
altura = float(input('altura: '))
imc = peso / altura ** 2

status = ["Fora da faixa", "Peso normal"]
resultado = status[18.5 <= imc <= 24.9]

print('Seu peso IMC é de: ', imc)
print('Resultado:' + resultado)