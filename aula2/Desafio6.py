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
