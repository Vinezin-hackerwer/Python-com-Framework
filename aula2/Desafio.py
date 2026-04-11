# Desafio:
# Contexto:
# Uma indústria monitora temperatura (T), umidade (U) e presença de gás inflamável (G, 0 ou 1).
# O nível de risco é dado por:

# Crítico: (T > 40 ou U > 80) e G == 1
# Alto: (T > 40 ou U > 80) e G == 0
# Médio: (T entre 25 e 40) e (U entre 50 e 80) e o  G == 0
# Baixo: qualquer outra situação

# Tarefa:
# Receba T (float), U (float), G (0 ou 1).
# Classifique o risco em "Crítico", "Alto", "Médio" ou "Baixo" sem usar if/elif.
# Use apenas dicionários com chaves booleanas e operadores lógico
# UTILIZE APENAS SINAIS LÓGICOS -  VARIAVEIS  -  LISTAS  -  I/O -  NÃO UTILIZE CONDICIONAIS OU LOOPS

t = int(input('Temperatura >>> '))
u = int(input('Umidade >>> '))
g = int(input('Gás >>>'))

v = ((t > 40 and u > 80 and g == 1) * 'Crítico') or ((t > 40 and u > 80 and g == 0) * 'Alto') or ((t > 25 or t < 40 and u >= 50 or u >=80 and g == 0) * 'Médio') or  'Baixo'

print(v)