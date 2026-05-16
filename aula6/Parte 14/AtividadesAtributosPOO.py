# # ### **Exercício 1 – Livro**

# # Crie uma classe `Livro` com atributos de instância: `titulo`, `autor`, `ano`, `emprestado` (booleano, padrão `False`). Métodos:

# # - `emprestar()` – se disponível, muda `emprestado` para `True`.
# # - `devolver()` – muda `emprestado` para `False`.
# # - `__str__()` – retorna uma string com as informações.
    
# #     Teste com dois livros.

# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo =  titulo
#         self.autor = autor
#         self.ano = ano
#         self.emprestado = False
        
#     def emprestar(self):
#         if not self.emprestado:
#             self.emprestado = True
#             return self.emprestado
            
            
#     def devolver(self):
#         self.emprestado = False         
#         return self.emprestado
    
#     def __str__(self):
#         return f'{self.titulo} {self.autor} {self.ano}'

# titulo, autor, ano = input('Livro: '), input('autor: '), input('ano ')

# l1 =  Livro(titulo, autor, ano)

# print('Emprestado? - ', l1.emprestar())

# print('Emprestado? - ',l1.devolver())

# print(l1)

# #-----------------------------------------------------

# ### **Exercício 2 – Contador com Atributo de Classe**

# # Crie uma classe `Contador` que tenha um atributo de classe `total_contadores` que conta quantas instâncias foram criadas.\
# #  Cada vez que um novo objeto é criado, esse contador deve ser incrementado. Adicione um método `exibir_total()` que exibe o total de contadores criados.


# class Contador:
#     total_contadores = 0
#     def __init__(self):
#         Contador.total_contadores += 1
        
#     def exibir_total(self):
#         print(Contador.total_contadores)
        
# c1 =  Contador()
# c2 =  Contador()
# c3 =  Contador()
# c4 =  Contador()
        

# c1.exibir_total()


# #-----------------------------------------------------

# ### **Exercício 3 – Produto com Desconto**

# # Classe `Produto` com atributos protegido55 `_nome`, `_preco`, `_quantidade`. Use propriedades (`@property`) para acessar esses atributos. \
# # Crie um método `aplicar_desconto(percentual)` que reduz o preço. O preço não pode ficar negativo. Teste criando produtos e aplicando descontos.


# class Produto:
#     def __init__(self, nome, preco, quantidade):
#         self._nome = nome
#         self._preco = preco
#         self._quantidade  =  quantidade
        
#     @property
#     def nome(self):
#         return self._nome
    
#     @property
#     def preco(self):
#         return self._preco
    
#     @property
#     def quantidade(self):
#          return self._quantidade
    
#     def aplicar_desconto(self, percentual):
#         desconto = self._preco * percentual
#         novo = self._preco  - desconto
#         if self._preco >= 0:
#             self._preco = novo
            
            

# p =  Produto('HD', 100.0,1)
# p.aplicar_desconto(0.10)
# print(p)
# print(p.nome, p.preco)        


# #-----------------------------------------------------

# # ### **Exercício 4 – Banco com Saldo Privado**

# # Classe `ContaBancaria` com atributo privado `__saldo`. Métodos:

# # - `depositar(valor)` – aumenta saldo.
# # - `sacar(valor)` – reduz saldo se houver saldo suficiente; senão, exibe mensagem.
# # - `exibir_saldo()` – retorna o saldo (use propriedade `saldo` apenas para leitura).
    
# #     Crie uma conta, realize operações e exiba o saldo.
# class ContaBancaria:
#     def __init__(self):
#         self.__saldo = 0


#     def teste(self):
#         return self.__saldo    
        
#     def depositar(self, valor):
#         self.__saldo += valor
        
#     def sacar(self, valor):
#         if valor <= self.__saldo:
#             self.__saldo -= valor
#         else:
#             print('Saldo insuficiente...')
        
#     # @property
#     # def saldo(self):
#     #     return self.__saldo


# conta  =  ContaBancaria()
# conta.depositar(1000)
# conta.sacar(500)


# # print(conta.teste())
# print(conta.__saldo)

# #-----------------------------------------------------

# ### **Exercício 5 – Aluno com Notas**

# # Classe `Aluno` com atributos: `nome`, `matricula` e uma lista privada `__notas`. Métodos:

# # - `adicionar_nota(nota)` – adiciona à lista (valida de 0 a 10).
# # - `calcular_media()` – retorna a média.
# # - `situacao()` – retorna "Aprovado" se média >= 7, "Recuperação" se >= 5, "Reprovado" caso contrário.
    
# #     Teste com um aluno e algumas notas.


# class Aluno:
#     def __init__(self, nome, matricula):
#         self.nome  = nome
#         self.matricula =  matricula 
#         self.__notas = []

#     def adcionar_notas(self, nota):
#         if 0 <= nota <= 10 :
#             self.__notas.append(nota)
            
#     def calcular_media(self):
#         if len(self.__notas) == 0:
#             return 0
#         return sum(self.__notas) / len(self.__notas)
    
#     def situacao(self):
#         media  =  self.calcular_media()
#         if media >= 7:
#             return 'Aprovado'
#         elif media >= 5:
#             return 'Recuperação'
#         else:
#             return 'Reprovado'

# aluno1 = Aluno('Ana', '1')
# aluno2 = Aluno('Julia', '2')

# aluno1.adcionar_notas(8)
# aluno1.adcionar_notas(5)
# aluno1.adcionar_notas(10)

# aluno2.adcionar_notas(1)
# aluno2.adcionar_notas(2.5)
# aluno2.adcionar_notas(10)

# print('Média',aluno1.nome ,aluno1.calcular_media())
# print('Média',aluno2.nome ,aluno2.calcular_media())

# print(aluno1.situacao())
# print(aluno2.situacao())


# #-----------------------------------------------------

# # ### **Exercício 6 – Data (validação)**

# # Crie uma classe `Data` com atributos `dia`, `mes`, `ano`. No `__init__`, valide se a data é válida\
# # (considere meses com 30/31 dias e ano bissexto para fevereiro). Use propriedades para garantir que alterações futuras também sejam validadas. Adicione um método `__str__` que retorna a data no formato `dd/mm/aaaa`.


# class Data:
#     def __init__(self, dia, mes, ano):
#         self.dia =  dia
#         self.mes  = mes 
#         self.ano =  ano

#     def __str__(self):
#         print(f'{dia}/{mes}/{ano}')    

#     def bissexto(self, ano):
#         if (ano % 400 == 0 or ano % 4 == 0) or (ano % 100 == 0):
#             print('ano bissexto...')
#         else:
#             print('Não é bissexto...')

#     def data_valida(self, dia, mes):
    
#         meses   =  [0,1,2,3,4,5,6,7,8,9,10,11,12]
#         dias_meses = [0,list(range(0,31)),
#                     list(range(1,29)),
#                     list(range(1,31)),
#                     list(range(1,30)),
#                     list(range(1,31)),
#                     list(range(1,30)),
#                     list(range(1,31)),
#                     list(range(1,31)),
#                     list(range(1,30)),
#                     list(range(1,31)),
#                     list(range(1,30)),
#                     list(range(1,31))
#                     ]
#         if mes in meses:
#            i =  meses.index(mes)
#         if dia in dias_meses[i]:
#            print('data válida')
#         else:
#            print('Data invalida')

# ano =  int(input('ano: '))
# mes =  int(input('Digite o número do mês: '))
# dia =  int(input('Digite o dia:  '))


# data  =  Data(dia, mes, ano)
# data.bissexto(ano)
# data.data_valida(dia, mes)
# data.__str__()


# #-----------------------------------------------------

# # ### **Exercício 7 – Funcionário com Aumento**

# # Classe `Funcionario` com atributos: `nome`, `cargo`, `salario_base` (privado). Métodos:

# # - `aumentar_salario(percentual)` – aumenta o salário.
# # - `calcular_bonus()` – retorna 10% do salário base.
# # - Propriedade `salario` para leitura.
    
# #     Teste criando um funcionário, aumente o salário e mostre o novo valor.
    

# class Funcionario:
#     def __init__(self, nome, cargo, salario):
#         self.nome  =  nome 
#         self.cargo =  cargo
#         self._salario_base =  salario

#     def aumentar_salario(self, percentual):
#         self._salario_base += self._salario_base * percentual / 100
#         return self._salario_base
    
#     def calcular_bonus(self):
#         return self._salario_base * 0.10

#     @property
#     def salario(self):
#         return self._salario_base

# salario = float(input('Salario: '))
# f  =  Funcionario('Ana', 'DEv', salario)
# aumento = f.aumentar_salario(0.10)
# bonus = f.calcular_bonus()           

# print(aumento + bonus )    


# #-----------------------------------------------------

# # ### **Exercício 8 – Carro com Velocidade (Encapsulamento)**

# # Classe `Carro` com atributos `marca`, `modelo` e `__velocidade` (inicial 0). Métodos:

# # - `acelerar(valor)` – aumenta velocidade até no máximo 200.
# # - `frear(valor)` – reduz velocidade até no mínimo 0.
# # - Propriedade `velocidade` para leitura.
    
# #     Teste acelerando e freando.
    

# class Carro:
#     def __init__(self, marca, modelo):
#         self.marca =  marca
#         self.modelo =  modelo
#         self.__velocidade =  0

#     def acelerar(self, valor):
#         self.__velocidade += valor
#         if self.__velocidade > 200:
#             self.__velocidade = 200

#     def frear(self, valor):
#         self.__velocidade -= valor
#         if self.__velocidade < 0:
#             self.__velocidade = 0

#     @property
#     def velocidade(self):
#         return self.__velocidade



# c  =  Carro('Ferrari', 'Ferrari')
# c.acelerar(50)
# c.acelerar(300)
# c.frear(100)

# print(c.velocidade)


# #-----------------------------------------------------

# # ### **Exercício 9 – Estatísticas (Atributos de Classe)**

# # Classe `Estatistica` com atributos de classe `soma` e `contagem`. Métodos de classe:

# # - `adicionar(valor)` – atualiza soma e contagem.
# # - `calcular_media()` – retorna a média (ou 0 se nenhum valor adicionado).
    
# #     Use `@classmethod` e não crie instâncias. Teste adicionando números e exibindo a média.



# class Estatistica: 

#     soma =  0
#     contagem = 0

#     @classmethod
#     def adcionar(cls, valor):
#         cls.soma  += valor
#         cls.contagem += 1

#     @classmethod
#     def calcular_media(cls):
#         if cls.contagem == 0:
#             return 0
#         return cls.soma/cls.contagem    

# Estatistica.adcionar(10)
# Estatistica.adcionar(5)
# Estatistica.adcionar(2)

# print(Estatistica.calcular_media())


# #-----------------------------------------------------

# ### **Exercício 10 – Agenda com Contatos (Composição)**

# # Crie uma classe `Contato` com atributos `nome`, `telefone`, `email`. Crie uma \
# # classe `Agenda` que possui uma lista privada de contatos. Métodos:

# # - `adicionar_contato(contato)` – adiciona à lista.
# # - `listar_contatos()` – exibe todos os contatos.
# # - `buscar_contato(nome)` – exibe os dados do primeiro contato com aquele nome.
    
# #     Teste adicionando vários contatos e fazendo buscas.

# class Contato():
#      def __init__(self, nome, telefone, email):
#           self.nome = nome
#           self.telefone =  telefone
#           self.email   =  email


# class Agenda():
#      def __init__(self):
#         self.__contatos =  []



#      def add_contato(self, contato):
#           self.__contatos.append(contato)


#      def lista_contato(self):
#           for c in self.__contatos:
#                print(c.nome, c.telefone, c.email)
     
#      def buscar_contato(self, nome):
#          for c in self.__contatos:
#               if c.nome == nome:
#                    print(c.nome, c.telefone,c.email)




# agenda  = Agenda()


# contato1 = Contato('ana','54464646', 'ana@gmail.com')


# contato2 = Contato('ana2','54464646', 'ana@gmail.com')


# agenda.add_contato(contato1)
# agenda.add_contato(contato2)
# agenda.lista_contato()
# agenda.buscar_contato('ana')

