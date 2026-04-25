def nome():
    return 'teste'

print(nome())    

# variável fora da função
n = 10
def soma():
    n  =  20
    return n

print(n)
print(soma())

# variaveis locais são criadas dentro da função 
# variaveis globais são criadas fora da função

# parametros
# padrão
def soma (a, b):
    return a +  b
soma (10,20)

# nomeados
def sub(a = 10 , b = 10):
    return a  +  b 
sub(200)

# pocisionais
def mult(a , b  =  200, c=0):
    return a * b * c 

def v_salario_hora(carga, salario=250):
    return salario / carga

salario_hora =  v_salario_hora(100,1010)
adicional =  salario_hora * 0.7
print(salario_hora +  adicional)