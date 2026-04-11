# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:
# "Criança" se idade < 12
# "Adolescente" se 12 ≤ idade ≤ 17
# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.

idade = int(input('Idade: '))

eh_crianca = (idade < 12)
eh_adolescente = (12 <= idade <= 17)
eh_adulto = (idade >= 18)

classificacao = ["Criança", "Adolescente", "Adulto"]
indice = (eh_adolescente * 1) + (eh_adulto * 2)

print(classificacao[indice])

