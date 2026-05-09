# ### **1. Classe Livro**
# Crie uma classe `Livro` com:

# - Atributos: `titulo`, `autor`, `ano`, `disponivel` (booleano, padrão True)
# - Métodos:
#     - `emprestar()`: se disponível, marca como False e exibe `"Livro emprestado"`; \
# senão, exibe `"Indisponível"`
#     - `devolver()`: marca como True e exibe `"Livro devolvido"`
#     - `info()`: mostra todas as informações do livro

#         Crie dois livros, faça empréstimos e devoluções.


# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo =  titulo
#         self.autor = autor
#         self.ano = ano
#         self.dispo = True

#     def emprestrar(self):
#       nome  = input('nome: ')
#     #   print(self.dispo)
#       emprestar =  input('Emprestar? ')
#       if emprestar == 'sim':
#         if nome  == self.titulo:
#             if self.dispo == True:
#                 print(self.dispo)
#                 print('esta disponivel ...')
#                 self.dispo = False
#                 print('Emprestado')
#                 return self.dispo

#             else:
#                 print('Não esta diponivel')
#         else:
#             print('Não temos esse livro...')
#     def devolver(self):
#         self.dispo = True
#         print('Livro devolvido')
#         return self.dispo
#     def info(self):
#         return [
#         self.titulo,
#         self.autor,
#         self.ano,
#         self.dispo 
#         ]


# livro =  Livro('Cisne negro', 'taleb','2012')
# livro.emprestrar()
# livro.devolver()
# print(livro.info())

# print('=================================================')

### **2. Classe Funcionário**

# Crie uma classe `Funcionario` com:

# - Atributos: `nome`, `cargo`, `salario_base`
# - Métodos:
#     - `aumentar_salario(percentual)`: aumenta o salário com base no percentual
#     - `calcular_bonus()`: retorna 10% do salário base
#     - `exibir_dados()`: exibe todas as informações
#         Crie um funcionário, aumente o salário e mostre os dados atualizados.

# class Funcionario:
#     def __init__(self, nome, cargo, salario_base):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario_base = salario_base

#     def aumentar_salario(self, percentual):
#         aumento = self.salario_base * (percentual / 100)
#         self.salario_base += aumento
#         print(f"\n>>> Salário de {self.nome} atualizado para R$ {self.salario_base:.2f}")

#     def exibir_dados(self):
#         print("\n--- Informações do Funcionário ---")
#         print(f"Nome: {self.nome}")
#         print(f"Cargo: {self.cargo}")
#         print(f"Salário Atual: R$ {self.salario_base:.2f}")
#         print("-" * 34)

# nome_usu = input("Digite o nome do funcionário: ")
# cargo_usu = input("Digite o cargo: ")
# salario_usu = float(input("Digite o salário base: R$ "))

# funcionario1 = Funcionario(nome_usu, cargo_usu, salario_usu)

# funcionario1.exibir_dados()

# pct_aumento = float(input(f"Qual o percentual de aumento para {funcionario1.nome} (ex: 10 para 10%): "))
# funcionario1.aumentar_salario(pct_aumento)

# funcionario1.exibir_dados()

# print('=================================================')

### **3. Classe Carro com Controle de Velocidade**

# Crie uma classe `Carro` com:
# - Atributos: `marca`, `modelo`, `velocidade` (inicial 0)
# - Métodos:
#     - `acelerar(valor)`: aumenta a velocidade (não pode ultrapassar 200 km/h)
#     - `frear(valor)`: diminui a velocidade (não pode ficar negativa)
#     - `velocidade_atual()`: exibe a velocidade
#         Crie um carro, acelere e freie até parar.

# class Carro:
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo
#         self.velocidade = 0

#     def acelerar(self, valor):
#         self.velocidade += valor
#         if self.velocidade > 200:
#             self.velocidade = 200
#             print("Limite atingido! O carro está a 200 km/h.")
#         else:
#             print(f"Acelerando... Velocidade atual: {self.velocidade} km/h")

#     def frear(self, valor):
#         self.velocidade -= valor
#         if self.velocidade < 0:
#             self.velocidade = 0
#             print("O carro parou (0 km/h).")
#         else:
#             print(f"Freando... Velocidade atual: {self.velocidade} km/h")

#     def velocidade_atual(self):
#         print(f"\n>>> [{self.marca} {self.modelo}] Velocidade: {self.velocidade} km/h\n")

# marca = input("Marca do carro: ")
# modelo = input("Modelo do carro: ")
# meu_carro = Carro(marca, modelo)

# valor_acelerar = int(input(f"Quanto deseja acelerar o {modelo}? "))
# meu_carro.acelerar(valor_acelerar)
# meu_carro.velocidade_atual()

# valor_frear = int(input("Quanto deseja frear? "))
# meu_carro.frear(valor_frear)
# meu_carro.velocidade_atual()

# print("Pisando fundo no freio...")
# meu_carro.frear(200) 
# meu_carro.velocidade_atual()

# print('=================================================')

### **4. Classe Agenda**

# Crie uma classe `Agenda` que armazena contatos. Cada contato é um objeto da classe `Contato` \
# (crie-a separada), com `nome`, `telefone` e `email`. A classe `Agenda` deve ter:

# - Atributo: `contatos` (lista)
# - Métodos:
#     - `adicionar_contato(contato)`: adiciona à lista
#     - `listar_contatos()`: exibe todos os contatos
#     - `buscar_contato(nome)`: exibe os dados do contato (se existir)
#         Crie alguns contatos, adicione-os à agenda e faça buscas.

# class Contato:
#     def __init__(self, nome, telefone, email):
#         self.nome = nome
#         self.telefone = telefone
#         self.email = email

#     def exibir(self):
#         print(f"Nome: {self.nome} | Tel: {self.telefone} | Email: {self.email}")


# class Agenda:
#     def __init__(self):
#         self.contatos = []

#     def adicionar_contato(self, contato):
#         self.contatos.append(contato)
#         print(f"Contato '{contato.nome}' adicionado com sucesso!")

#     def listar_contatos(self):
#         print("\n--- Lista de Contatos ---")
#         if not self.contatos:
#             print("A agenda está vazia.")
#         else:
#             for c in self.contatos:
#                 c.exibir()
#         print("-" * 25)

#     def buscar_contato(self, nome_busca):
#         print(f"\nBuscando por: {nome_busca}...")
#         encontrado = False
#         for c in self.contatos:
#             if c.nome.lower() == nome_busca.lower():
#                 c.exibir()
#                 encontrado = True
#                 break
        
#         if not encontrado:
#             print("Contato não encontrado.")

# minha_agenda = Agenda()

# c1 = Contato("Ana Silva", "11-98888-7777", "ana@email.com")
# c2 = Contato("Carlos Souza", "21-97777-6666", "carlos@email.com")
# c3 = Contato("Beatriz Lima", "13955554444", "beatriz@empresa.com")

# minha_agenda.adicionar_contato(c1)
# minha_agenda.adicionar_contato(c2)

# minha_agenda.listar_contatos()

# nome_procurado = input("Digite o nome que deseja buscar na agenda: ")
# minha_agenda.buscar_contato(nome_procurado)

# print('=================================================')
