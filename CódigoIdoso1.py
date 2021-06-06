import datetime

nomes = []
idades = []

for count in range(1, 4):
    nome = input('-> Nome: ')
    nascimento = input('-> Data de Nascimento DD/MM/AAAA: ')
    day, month, year = map(int, nascimento.split('/'))
    dia, mes, ano = int(day), int(month), int(year) # Tive que converter dia, mês e ano para inteiro
    while dia > 28 and mes == 2 or mes > 12 or mes <= 0 or dia > 31 or dia <= 0 or ano == 2021 and mes > datetime.date.today().month or ano > 2021: #Apresenta mensagem caso alguma dessas informações seja informada
        print(f'{"=" * 32}\nAlguma Coisa Está Errada Aí!\nPossíveis Erros:\n- Dia Maior Que 31 (Caso Mês Seja Fevereiro Dia Maior Que 28).\n- Mês Maior Que 12 / Mês Maior No Ano Atual.\n- Ano Maior Que Atual.\n{"=" * 32}')
        nascimento = input('-> Data de Nascimento DD/MM/AAAA: ')
        day, month, year = map(int, nascimento.split('/'))
        dia, mes, ano = int(day), int(month), int(year)
    else:
        idade = datetime.date.today().year - int(year) #Diminui o ano de nascimento informado do ano atual, que é gerado automaticamente pelo datetime para sabermos a idade.
        idades.append([ano, mes, dia])  #Adicionei as variáveis de nascimento em uma lista para percorre-las e informar o mais velho

        if 60 <= idade <= 74:
            situation = 'Idoso' #Usei uma variável chamada situation para informar se a pessoa é idosa
        else:
            situation = ''

        nomes.append([nome, nascimento, situation])

print('=' * 40)
print('Pessoas Informadas')
print('=' * 40)
for k, v in enumerate(nomes):
    print(f'Nome: {v[0]}\nData de Nascimento: {v[1]}\n{v[2]}')
    print('=' * 40)
