# jogo com programação
# pedra papel com POO
import random

# jogador
class Jogador:
    def escolher(self):
        escolha = input('Escolha pedra,papel ou tesoura')
        return escolha.lower()
# computador
class Computador:
    def escolher(self):
        opcao = ['pedra','papel','tesoura']
        return random.choice(opcao)
    
class Jogo:

    def verificar_vencedor(self, jogador, computador):
        score_jogador = 0
        score_computador = 0
        if jogador == computador:
            print(score_jogador, 'x', score_computador)
            return 'empate'
        if jogador == 'pedra' and computador == 'tesoura':
            score_jogador =  score_jogador + 1
            print(score_jogador, 'x', score_computador)
            return 'Jogador venceu'
        elif jogador == 'tesoura' and computador  == 'papel':
            score_jogador =  score_jogador + 1
            print(score_jogador, 'x', score_computador)
            return 'Jogador venceu'
        elif jogador == 'papel'  and computador == 'pedra':
            score_jogador =  score_jogador + 1
            print(score_jogador, 'x', score_computador)
            return 'Jogador venceu'
        else:
            score_computador =  score_computador + 1
            print(score_jogador, 'x', score_computador)
            print()
            return 'Computador venceu...'
    def jogar(self):
            
            while True:
                jogador  = Jogador()
                computador = Computador()
                escolha_jogador  = jogador.escolher()
                escolha_computador  = computador.escolher()
                print('Jogador escolheu - ', escolha_jogador)
                print('Computador escolheu - ', escolha_computador)
                resultado = self.verificar_vencedor(escolha_jogador, escolha_computador)
                print('RESULTADO', resultado)
        
jogo = Jogo()
jogo.jogar()

# -------------------------------------------------------------------

