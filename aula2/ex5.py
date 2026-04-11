# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade e o peso.
# Para doar sangue, a pessoa deve ter entre 16 e 69 anos (inclusive) e 
# pesar pelo menos 50 kg.
# Use and para verificar ambos os critérios e informe se a pessoa pode doar.

idade = int(input('Idade: '))
peso = float(input('Peso (kg): '))

pode_doar = (16 <= idade <= 69 and peso >= 50)
mensagens = ["Não pode doar sangue", "Pode doar sangue"]

print(mensagens[pode_doar])
