# ### **5. Jogo de Pedra, Papel e Tesoura**

# Leia duas jogadas (`"pedra"`, `"papel"` ou `"tesoura"`) e determine o vencedor ou empate. Use condicionais aninhadas.

print("=====================================")
print("1 - Pedra // 2 - Papel // 3 - Tesoura")
print("=====================================")

j1 = int(input("Jogador 1 - Digite a sua escolha: "))
print("=====================================")
j2 = int(input("Jogador 2 - Digite a sua escolha: "))
print("=====================================")

if j1 == 1 and j2 == 1 or j1 == 2 and j2 == 2 or j1 == 3 and j2 == 3:
    print("Empate!")
elif j1 == 1 and j2 == 3 or j1 == 2 and j2 == 1 or j1 == 3 and j2 == 2:
    print("O Jogador 1 venceu!")
elif j2 == 1 and j1 == 3 or j2 == 2 and j1 == 1 or j2 == 3 and j1 == 2:
    print("O Jogador 2 venceu!")