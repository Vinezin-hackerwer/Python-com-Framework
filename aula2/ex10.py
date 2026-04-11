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
