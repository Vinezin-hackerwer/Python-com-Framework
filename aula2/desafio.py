# Desafio aula 5:
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
g = int(input('Gás >>> '))

v = ((t > 40 and u > 80 and g == 1) * 'Crítico') or ((t > 40 and u > 80 and g == 0) * 'Alto') or ((t > 25 or t < 40 and u >= 50 or u >=80 and g == 0) * 'Médio') or  'Baixo'

print(v)

# =============================================================================
print("============================================================================")
print("============================================================================")

# Desafio aula 6:
# Use dicionário, variáveis ou listas … 
# Contexto:
# Uma loja oferece um cupom especial. O cliente ganha o cupom se atender a pelo menos  das seguintes condições:

# Se for VIP (responde "sim" ou "não")
# Valor da compra acima de R$ 200
# Primeira compra no mês (responder "sim" ou "nao")
# Além disso, o cupom  pode ser aplicado se o cliente tiver  no histórico. 

# Tarefa Receba:
# vip (string "sim" ou "nao")
# valor (float)
# primeira_compra (string "sim" ou "nao")
# Reclamação 
# Determine se o cliente  ("Cupom liberado") ou  ("Sem cupom"),  (SEM IF , SEM LOOP, SEM FUNÇÃO)

vip = input('É VIP? (sim/nao): ') == 'sim'
valor = float(input('Valor da compra: '))
primeira_compra = input('Primeira compra no mês? (sim/nao): ') == 'sim'
reclamacao = input('Tem reclamação no histórico? (sim/nao): ') == 'sim'

condicao_cupom = (vip or valor > 200 or primeira_compra) and not reclamacao

resultado = {
    True: "Cupom liberado",
    False: "Sem cupom"
}

print(resultado[condicao_cupom])
