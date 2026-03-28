# # 4 tipos primitivos
# # variável
# # Sinais aritméticos
# # Sinais lógicos 




# Peça o valor de um produto e:
produto = float(input('Digite o valor do produto: '))


# Calcule um desconto de 10%.


desconto = produto * 0.10


print('Desconto', desconto)



# Mostre o valor final.


# Verifique se o valor final é maior que 100.


# Verifique se o produto ficou barato (menor que 50).





print('================================')
print('Churros da Dona Florinda!')

print('================================')

print('Valor total da compra: ')
valor = int(input('Digite o valor da compra: '))

desconto = 0.10
total = valor - (valor * desconto) 

print('================================')
print('Valor total com desconto de 10% no pix: ', total)
print('================================')
print('O valor é acima de R$100? ', total > 100)
print('O valor é abaixo de R$50? ', total < 50)
print('================================')