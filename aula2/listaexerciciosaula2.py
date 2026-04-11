# =============================================================================
print("============================================================================")
print("============================================================================")

# 1. Verificação de maioridade e permissão
# Enunciado:
# Crie um programa que leia a idade do usuário e se ele possui autorização dos pais 
# (responda True ou False).
# O usuário pode participar da atividade se tiver 18 anos ou mais ou 
# tiver autorização dos pais.
# Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".


idade = int(input('idade: '))
autorizacao = input('Autoriza True ou False')

verificar = idade >= 18 or bool(autorizacao == 'True') and 'Pode participar' or 'Não pode participar'

print(verificar)

# =============================================================================
print("============================================================================")
print("============================================================================")


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


# =============================================================================
print("============================================================================")
print("============================================================================")

# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário 
# for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" 
# ou "Acesso negado".

usuario = input('Usuário: ')
senha = input('Senha: ')

acesso_permitido = (usuario == "admin" and senha == "1234")
mensagens = ["Acesso negado", "Acesso liberado"]

print(mensagens[acesso_permitido])


# =============================================================================
print("============================================================================")
print("============================================================================")


# 4. Compra com desconto
# Enunciado:
# Leia o valor da compra e se o cliente é VIP (True ou False).
# O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.
# Exiba o valor final com desconto (se aplicável) ou o valor original.

valor = float(input('Valor da compra (R$): '))
is_vip = input('O cliente é VIP? (True/False): ') == "True"

ganha_desconto = (valor > 100 or is_vip)
valor_final = valor - (valor * 0.10 * ganha_desconto)

print(f"Valor final: R$ {valor_final:.2f}")


# =============================================================================
print("============================================================================")
print("============================================================================")


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


# =============================================================================
print("============================================================================")
print("============================================================================")


# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar 
# sábado/domingo como fechado.

dia = int(input('Dia da semana (1-Segunda a 7-Domingo): '))
hora = int(input('Hora atual (0-23): '))

esta_aberta = (1 <= dia <= 5) and (9 <= hora < 18)
status = ["Loja fechada", "Loja aberta"]

print(status[esta_aberta])


# =============================================================================
print("============================================================================")
print("============================================================================")


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


# =============================================================================
print("============================================================================")
print("============================================================================")


# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que 
# também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".

ano = int(input('Digite o ano: '))

eh_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
status = ["Ano não bissexto", "Ano bissexto"]

print(status[eh_bissexto])


# =============================================================================
print("============================================================================")
print("============================================================================")


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


# =============================================================================
print("============================================================================")
print("============================================================================")


# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.

temp = float(input('Temperatura (°C): '))
umidade = float(input('Umidade (%): '))

alerta_ativo = (temp > 35 or umidade > 70)
status = ["Condições normais", "ALERTA: Risco detectado!"]
 
print(status[alerta_ativo])


# =============================================================================
print("============================================================================")
print("============================================================================")


try:
    a = int(input('>>>'))
    b = int(input('>>>'))
    lista  =  [a,b]
    print(a/b)
    i  =  int(input('Digite um indice da lista: '))
    print(lista[i])
except ZeroDivisionError as erro:
    print(erro)
except ValueError as erro :
    print(erro)
except TypeError as erro:
    print(erro)
except IndexError as erro:
    print(erro)
else:
    print('Erro não identificado') 
finally:
    print('Fim de carregamento ...')               


# =============================================================================
print("============================================================================")
print("============================================================================")
