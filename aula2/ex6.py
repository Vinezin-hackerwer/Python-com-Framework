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
