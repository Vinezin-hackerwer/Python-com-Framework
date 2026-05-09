# Crie uma classe Pessoa com os atributos nome e idade. z
# Adicione um método apresentar() que exiba "Olá, meu nome é [nome] e tenho [idade] anos."z
#  Crie duas pessoas diferentes e chame o método.

# criei a classe
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade  = idade
# # criei o método
#     def apresentar(self):
#         print(f'Olá, meu nome é {self.nome}, eu tenho {self.idade}')
# # instaciei a classe
# pessoa1 =  Pessoa('Kaio',20)
# pessoa2 =  Pessoa('Maria',22)
# # usei o método na instancia 
# pessoa1.apresentar()
# pessoa2.apresentar()

# print("========================================================")

# ### **2.Classe Retângulo**

# Crie uma classe `Retangulo` com os atributos `largura` e `altura`. Adicione métodos:

# - `calcular_area()` – retorna a área
# - `calcular_perimetro()` – retorna o perímetro
    
#     Crie um retângulo com largura 5 e altura 3 e exiba sua área e perímetro.

# class Retangulo:
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura

#     def calcular_area(self):
#         return self.largura * self.altura

#     def calcular_perimetro(self):
#         return 2 * (self.largura + self.altura)

# l = float(input("Digite a largura do retângulo: "))
# a = float(input("Digite a altura do retângulo: "))

# ret = Retangulo(l, a)
# print(f"Área: {ret.calcular_area()} | Perímetro: {ret.calcular_perimetro()}")

# print("========================================================")

# ### **3.   Classe Conta Bancária**

# Crie uma classe `ContaBancaria` com:

# - Atributos: `titular`, `saldo` (inicial 0)
# - Métodos:
#     - `depositar(valor)`: acrescenta ao saldo
#     - `sacar(valor)`: se houver saldo suficiente, subtrai; senão, exibe `"Saldo insuficiente"`
#     - `exibir_saldo()`: mostra o saldo formatado
        
#         Crie uma conta, faça depósitos e saques e exiba o saldo.

# class ContaBancaria:
#     def __init__(self, titular):
#         self.titular = titular
#         self.saldo = 0

#     def depositar(self, valor):
#         self.saldo += valor
#         print(f"Depósito de R$ {valor:.2f} realizado.")

#     def sacar(self, valor):
#         if valor <= self.saldo:
#             self.saldo -= valor
#             print(f"Saque de R$ {valor:.2f} realizado.")
#         else:
#             print("Saldo insuficiente!")

#     def exibir_saldo(self):
#         print(f"Titular: {self.titular} | Saldo Atual: R$ {self.saldo:.2f}")

# nome = input("Digite o nome do titular: ")
# minha_conta = ContaBancaria(nome)

# v_deposito = float(input("Digite o valor para depósito: "))
# minha_conta.depositar(v_deposito)

# v_saque = float(input("Digite o valor para saque: "))
# minha_conta.sacar(v_saque)

# minha_conta.exibir_saldo()

# print("========================================================")

# ### **4. Classe Produto**

# Crie uma classe `Produto` com:

# - Atributos: `nome`, `preco`, `quantidade_estoque`
# - Métodos:
#     - `total_estoque()`: retorna `preco * quantidade_estoque`
#     - `adicionar_estoque(quantidade)`: aumenta a quantidade
#     - `remover_estoque(quantidade)`: diminui, mas não permite ficar negativo
        
#         Crie um produto, altere o estoque e exiba o valor total.

# class Produto:
#     def __init__(self, nome, preco, quantidade_estoque):
#         self.nome = nome
#         self.preco = preco
#         self.quantidade_estoque = quantidade_estoque

#     def total_estoque(self):
#         return self.preco * self.quantidade_estoque

#     def adicionar_estoque(self, quantidade):
#         self.quantidade_estoque += quantidade
#         print(f"{quantidade} unidades adicionadas. Novo estoque: {self.quantidade_estoque}")

#     def remover_estoque(self, quantidade):
#         if quantidade <= self.quantidade_estoque:
#             self.quantidade_estoque -= quantidade
#             print(f"{quantidade} unidades removidas. Novo estoque: {self.quantidade_estoque}")
#         else:
#             print(f"Erro: Estoque insuficiente! Você só tem {self.quantidade_estoque} unidades.")


# nome_p = input("Nome do produto: ")
# preco_p = float(input("Preço unitário: "))
# qtd_p = int(input("Quantidade inicial em estoque: "))

# p = Produto(nome_p, preco_p, qtd_p)

# add = int(input(f"Quanto de {p.nome} deseja ADICIONAR ao estoque? "))
# p.adicionar_estoque(add)


# rem = int(input(f"Quanto de {p.nome} deseja REMOVER do estoque? "))
# p.remover_estoque(rem)

# print(f"\nResumo Final:")
# print(f"Produto: {p.nome}")
# print(f"Quantidade atual: {p.quantidade_estoque}")
# print(f"Valor total em estoque: R$ {p.total_estoque():.2f}")

# print("========================================================")

# ### **5. Classe Aluno**

# Crie uma classe `Aluno` com:

# - Atributos: `nome`, `matricula`, `notas` (lista de floats)
# - Métodos:
#     - `adicionar_nota(nota)`: adiciona à lista
#     - `calcular_media()`: retorna a média das notas
#     - `situacao()`: retorna `"Aprovado"` se média >= 7, `"Recuperação"` se >= 5, `"Reprovado"` caso contrário
        
#         Crie um aluno, adicione 3 notas e exiba sua situação.

# class Aluno:
#     def __init__(self, nome):
#         self.nome = nome
#         self.notas = []

#     def adicionar_nota(self, nota):
#         self.notas.append(nota)

#     def calcular_media(self):
#         return sum(self.notas) / len(self.notas) if self.notas else 0

#     def situacao(self):
#         m = self.calcular_media()
#         if m >= 7: return "Aprovado"
#         elif m >= 5: return "Recuperação"
#         else: return "Reprovado"

# nome_aluno = input("Nome do aluno: ")
# aluno = Aluno(nome_aluno)

# for i in range(3):
#     n = float(input(f"Digite a nota {i+1}: "))
#     aluno.adicionar_nota(n)

# print(f"\nResultado final de {aluno.nome}:")
# print(f"Média: {aluno.calcular_media():.1f}")
# print(f"Situação: {aluno.situacao()}")

# print("========================================================")