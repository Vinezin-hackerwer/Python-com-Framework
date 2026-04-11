# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário 
# for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" 
# ou "Acesso negado".

usuario = input('Usuário: ')
senha = input('Senha: ')

acesso_permitido = (usuario == "admin" and senha == "1234")
mensagens = ["Acesso negado", "Acesso liberado"]

print(mensagens[acesso_permitido])
