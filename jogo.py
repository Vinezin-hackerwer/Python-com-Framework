# jogo de advinhação
import random

lista_pc = ['😂', '🤷‍♂️', '💖', '🤞']
nossa_lista = ['😂', '🤷‍♂️', '💖', '🤞']
aleatorio = random.choice(lista_pc)
escolha_personagem = input('teste: ')
resultado = aleatorio == escolha_personagem


print('Acertou? - ', resultado)
print('Escolhada maquina - ', aleatorio)
print('Minha escolha? - ', escolha_personagem)