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


dados = {
'vip': 0,
'valor_compra':0,
'primeira_compra':0,
'reclamação':0
}

vip = input('Vip - sim ou não')
valor_compra = float(input('R$ '))
primeira_compra = input('Primeira compra s/n')
reclamacao = input('True or False')

dados['primeira_compra'] = vip
dados['reclamação'] = reclamacao
dados['valor_compra'] = valor_compra
dados['vip'] = vip

v1 = dados['vip'] == 'sim'
v2 = dados['valor_compra'] > 200
v3 = dados['reclamação'] == 'False'
v4 = dados['primeira_compra'] = 'sim'

verificao = (v1 and v2 and v3 and bool(v4)) and 'Cumpom liberado' or 'Sem cupom'

print(verificao)