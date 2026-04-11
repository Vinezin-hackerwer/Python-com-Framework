# Primitivos 

# Crie um sistema onde precisamos verifica a idade do usuario
# se é maior de idade


# idade  = int(input('Idade: '))

# # verificação
# # and - e  or - ou  not - não
# # sinais aritméticos  ----  matemática  -  + | - | * |  / | // | % 
# # sinais lógicos  ----                  > |  <  |  >= | <= |  == | 
# print(idade >= 18)

# # True -  1
# # False -  0


# verifico =  idade >= 18 and 'Maior de idade' or 'Menor de idade'
                  
# print(verifico)


# idade =  25
# nome  = 'José'
# logica =  True
# real_decimal = 5.2

# tomando a decisão 

# conta_banco = float(input('>>>'))

# verifico2 = conta_banco <= 0 and 'conta zerada' or f'Possui valor {conta_banco}'

# print(verifico2)


# verificar senha para entrar no sistema


# senha  = input('digite sua senha: ')


# verificao3 = senha and senha == '1234' and 'Acesso autorizado' or 'acesso negado'

# print(verificao3)



# h = int(input('Hora: '))
# dia_semana =  int(input('Dia da Semana: '))
# v =  h > 8 and h < 19 and dia_semana >0 and  dia_semana <6 and 'Aberto' or 'fechado'
# print(v)





# 1. Verificação de maioridade e permissão
# Enunciado:
# Crie um programa que leia a idade do usuário e se ele possui autorização dos pais 
# (responda True ou False).
# O usuário pode participar da atividade se tiver 18 anos ou mais ou 
# tiver autorização dos pais.
# Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".



# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba 
# "Peso normal" ou "Fora da faixa".

# peso =  float(input('Peso: '))
# altura  =  float(input('Altura: '))

# imc  =  peso/(altura**2)
# v  = imc > 18.5 and imc <24.9 and 'PESO NORMAL' or 'FORA DA FAIXA' 
# print(v)


# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário 
# for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" 
# ou "Acesso negado".




# nome = input('Digite o usuário: ')
# senha = int(input('Senha: '))
# v  =  (nome == 'admin' and senha == 1234) and 'Acesso autorizado' or 'Acesso Negado'
# print(v)



# 4. Compra com desconto
# Enunciado:
# Leia o valor da compra e se o cliente é VIP (True ou False).
# O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.
# Exiba o valor final com desconto (se aplicável) ou o valor original.

# valor  =  float(input('R$ '))
# vip  = input('Pessoa é Vip? : True ou False: ')
# v  =  (valor > 100 or vip == 'True') and f'Desconto aplicado R$ {valor*0.10}' or f'Valor originar{valor} '
# print(v)


# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade e o peso.
# Para doar sangue, a pessoa deve ter entre 16 e 69 anos (inclusive) e 
# pesar pelo menos 50 kg.
# Use and para verificar ambos os critérios e informe se a pessoa pode doar.

# peso =  float(input('Peso: '))
# idade  =  int(input('idade: '))

# v  =  peso >= 50 and idade >= 16 and idade <= 69 and 'Pode doar' or 'Não pode doar'
# print(v)


# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar 
# sábado/domingo como fechado.

# dia  =  4
# hora =  13
# v = (dia >=1 and dia <6 and hora >8 and hora <19) and 'Aberta' or 'fechada'
# print(v)

# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que 
# também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".


# ano  =  1996

# bissexto = ((ano % 4 == 0 and ano % 400==0) or not ano % 100 == 0) and 'bissexto' or 'não é bissexto'
# print(bissexto)  


# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:

# "Criança" se idade < 12

# "Adolescente" se 12 ≤ idade ≤ 17

# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.


# idade  =  20
# v =  (idade <= 12 and 'criança' or idade > 12 and idade <= 17 and 'Adolescente') or 'adulto'
# print(v)


# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.


# temp =  float(input('Temperatura: '))
# umidade =  float(input('umidade: '))

# v =  (temp > 35 or umidade > 70 ) * 'Alerta' or 'Condições normais'
#       # True or false 
#          # 1 0

# print(v)




# Contexto:

# Uma indústria monitora temperatura (T), umidade (U) e presença de 
# gás inflamável (G, 0 ou 1).

# O nível de risco é dado por:

# Crítico: (T > 40 ou U > 80) e G == 1
# Alto: (T > 40 ou U > 80) e G == 0
# Médio: (T entre 25 e 40) e (U entre 50 e 80) e o  G == 0
# Baixo: qualquer outra situação

t  = int(input(' Temperatura >>>'))
u  = int(input('Umidade >>> '))
g  = int(input('Gás >>>'))

v = ((t > 40 and u > 80 and g == 1) * 'Crítico') or ((t > 40 and u > 80 and g == 0) * 'Alto') or ((t > 25 or t < 40 and u >= 50 or u >=80 and g == 0) * 'Médio') or  'Baixo'

print(v)




