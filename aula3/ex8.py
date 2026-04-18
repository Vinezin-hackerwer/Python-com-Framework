# ### **8. Escolha de Plano de Saúde**

# Leia a idade do cliente e o tipo de plano (`"basico"`, `"standard"`, `"premium"`). O valor mensal é calculado como:

# - Básico: R$ 100 + (idade * 2)
# - Standard: R$ 150 + (idade * 3)
# - Premium: R$ 200 + (idade * 5)
    
#     Se o cliente tiver mais de 60 anos, há um acréscimo de 10% sobre o valor total.

idade = int(input('idade: '))
plano =  input('PLano: basico/ standard/premium  ')

if plano == 'basico':
    valor  = 100 + idade * 2
    print('R$', valor)
    if idade > 60:
        n_v =  valor * 0.10
        valor  =  valor + n_v
        print('R$',valor)
elif plano == 'standard':
    valor  =  150 + idade * 3
    print('R$', valor)    
    if idade > 60:
        n_v =  valor * 0.10
        valor  =  valor + n_v
        print('R$',valor)        
elif plano == 'standard':
    valor  =  200 + idade * 5         
    print('R$', valor)
    if idade > 60:
        n_v =  valor * 0.10
        valor  =  valor + n_v
        print('R$',valor)    
        
