# import streamlit as st
# import pandas as pd

# dados  =  {
# 'Dia': ['Jan','Fev','Mar'],
# 'Vendas':[5000.0,1000.0,9000.0]
# }

# df =  pd.DataFrame(dados)

# if st.button('Gerar Grafico'):
#     st.bar_chart(df.set_index('Dia'))

# df2 =  pd.read_csv('vendas.csv')

# if st.button('Gerar grafico'):
#     st.bar_chart(df2, x = 'vendedor', y = 'venda')
#     st.table(df2)

# ---------------------------------------------------------------

# import streamlit as st
# from abc import ABC, abstractmethod
# import datetime

# st.set_page_config(page_title='POO e Streamlit')
# st.title('Laboratório de testes')

# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo =  titulo
#         self.autor = autor
#         self.ano = ano
#         self.lista  = []
    
#     def cadastro_livro(self):
#         self.lista.extend([self.titulo, self.autor, self.ano])
#         return self.lista
#     def __str__(self):
#         st.write(self.lista)
#         print(self.lista)


# nome  = st.text_input('Digite o nome do livro')
# autor = st.text_input('Digite o nome do autor')
# ano = st.date_input('Digite o ano')
# l = Livro(nome, autor, ano)
# l.cadastro_livro()


# if st.button('Salvar na lista'):

#     st.success('Dado cadastrado') 
# l.__str__()

#---------------------------------------------------


    ################
    ## PORTIFOLIO ##
    ################


import streamlit as st

st.set_page_config(page_title="Meu Portfólio Simples", page_icon="💼")
st.title("Meu Portfólio em POO")

class Portfolio:
    def __init__(self, nome, github, imagem, email, whatsapp, endereco, audio):
        self.nome = nome
        self.github = github
        self.imagem = imagem
        self.email = email
        self.whatsapp = whatsapp
        self.endereco = endereco
        self.audio = audio

    def mostrar_dados(self):
        st.image(self.imagem, width=500)
        
        st.subheader(f"Nome: {self.nome}")
        st.write(f"**GitHub:** {self.github}")
        st.write(f"**E-mail:** {self.email}")
        st.write(f"**WhatsApp:** {self.whatsapp}")
        st.write(f"**Endereço:** {self.endereco}")
        
        st.write("**Áudio de Apresentação:**")
        st.audio(self.audio)


nome_input = "Vinizin Apelaun"
github_input = "https://github.com/Vinezin-hackerwer"
imagem_input = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyTPEhcFWyKFNWPrlHOpDE1cLNgXRI0MO4Dw&s" 
email_input = "deiteinobru@yahoo.com"
whatsapp_input = "+55 (11) 4022-8922"
endereco_input = "Rua das ruas, nº 67 - Grajaú/SP"
audio_input = "teste.mp3" 

#imagem reserva:
# https://images.unsplash.com/photo-1618336753974-aae8e04506aa?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D

p = Portfolio(nome_input, github_input, imagem_input, email_input, whatsapp_input, \
    endereco_input, audio_input)

if st.button('Carregar Portfólio'):
    st.success('Portfólio carregado com sucesso!')
    p.mostrar_dados()
