# 7. Aprovação em duas disciplinas
# Enunciado:
# Leia as notas de Matemática e Português.
# O aluno é aprovado se ambas as notas forem maiores ou iguais a 6.
# Use and para verificar e exiba "Aprovado" ou "Reprovado".

nota_mat = float(input('Nota de Matemática: '))
nota_port = float(input('Nota de Português: '))

aprovado = (nota_mat >= 6 and nota_port >= 6)
status = ["Reprovado", "Aprovado"]

print(status[aprovado])
