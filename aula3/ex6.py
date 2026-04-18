# ### **6. Aprovação com Recuperação**

# Leia a nota da N1 e N2. Calcule a média (`(N1+N2)/2`). Se média ≥ 7, aprovado. Se média < 4, reprovado. Caso contrário, o aluno vai para recuperação. \
# Nesse caso, leia a nota da recuperação (NR). A média final é `(média + NR)/2`. Se média final ≥ 5, aprovado; senão, reprovado.

nt1 = float(input("Digite a sua primeira nota: "))
nt2 = float(input("Digite a sua segunda nota: "))
nr = 0

med = (nt1 + nt2) / 2
nf = (med + nr) / 2

if med >= 7:
    print("Aprovado! Sua média foi de: ", med)

elif med >=4 and med < 7:
    nr = float(input("Digite a sua nota de recuperação: "))
    
    nf = (med + nr) / 2
    if nf >= 5:
        print("Aprovado! Sua média com NR foi de: ", nf)
    else:
        print("Reprovado! Sua média com NR foi de: ", nf)
        
else:
    print("Reprovado! Sua média foi de:", med)