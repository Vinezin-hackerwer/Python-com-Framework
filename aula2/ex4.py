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
