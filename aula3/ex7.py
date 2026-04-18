### **7. Alistamento Militar**

# Leia o ano de nascimento, o sexo (`M` ou `F`) e se o usuário possui alguma deficiência impeditiva (`sim` ou `não`).

# - Se sexo for `F`, exiba `"Não obrigatório"`.
# - Se sexo for `M`, calcule a idade. Se idade < 18, exiba o tempo restante. Se idade = 18, exiba `"Aliste-se imediatamente"`. Se idade > 18 e ≤ 45, exiba `"Já passou do prazo"`. Se idade > 45, exiba `"Dispensado por idade"`.
# - Se houver deficiência, altere a mensagem para `"Dispensado por condição de saúde"` (prioridade sobre outras mensagens).

deficiencia = input('POssui deficiencia s/n?')
ano_n =  int(input('ano: '))
sexo = input('F/M')



if sexo == 'f':
    print('Não obrigatório...')
elif sexo == 'm':
    idade =  2026 - ano_n
    
    if deficiencia == 's':
        print('dispensado por condição de saúde')
    if idade == 18 and deficiencia == 'n':
        print('Aliste -se imediatamente')
    elif idade >18  and idade <= 45:
        print('Já passou do prazo')

