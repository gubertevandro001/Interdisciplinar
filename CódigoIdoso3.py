import datetime

nomes = []
idades = []
infos = True

while infos:
    nome = input('-> Nome: ')
    if nome == 'FIM' or nome == 'fim':
        break
    nascimento = input('-> Data de Nascimento DD/MM/AAAA: ')
    day, month, year = map(int, nascimento.split('/'))
    dia, mes, ano = int(day), int(month), int(year) #Tive que converter dia, mês e ano para inteiro
    while dia > 28 and mes == 2 or mes > 12 or mes <= 0 or dia > 31 or dia <= 0 or ano == 2021 and mes > datetime.date.today().month or ano > 2021: #Apresenta mensagem caso alguma dessas informações seja informada
        print(f'{"=" * 32}\nAlguma Coisa Está Errada Aí!\nPossíveis Erros:\n- Dia Maior Que 31 (Caso Mês Seja Fevereiro Dia Maior Que 28).\n- Mês Maior Que 12 / Mês Maior No Ano Atual.\n- Ano Maior Que Atual.\n{"=" * 32}')
        nascimento = input('-> Data de Nascimento DD/MM/AAAA: ')
        day, month, year = map(int, nascimento.split('/'))
        dia, mes, ano = int(day), int(month), int(year)
    else:
        idade = datetime.date.today().year - int(year) #Diminui o ano de nascimento informado do ano atual, que é gerado automaticamente pelo datetime para sabermos a idade.
        idades.append([ano, mes, dia])  #Adicionei as variáveis de nascimento em uma lista para percorre-las e informar o mais velho

        if idade < 45:
            class_oms = 'Não Informada'
            situation = '' #Usei uma variável chamada situation para informar se a pessoa é idosa
        elif 45 <= idade < 60:
            class_oms = 'Meia-Idade' #class_oms referente a classificação da oms
            situation = ''
        elif 60 < idade <= 74:
            class_oms = 'Idoso'
            situation = 'Idoso'
        elif 74 < idade <= 90:
            class_oms = 'Ancião'
            situation = ''
        else:
            class_oms = 'Velhice Extrema'
            situation = ''

        nomes.append([nome, nascimento, situation, class_oms])

mais_velho = idades.index(min(idades)) #Pega da lista idades os índices ano, mês e dia, calcula e informa o mais velho

print('=' * 40)
print('Pessoas Informadas')
print('=' * 40)
for k, v in enumerate(nomes):
    print(f'Nome: {v[0]}\nData de Nascimento: {v[1]}\n{v[2]}') #O índice v[2] só aparecerá caso a pessoa for idosa
    print('=' * 40)
print('===== Pessoa Mais Velha =====')
print(f'Nome: {nomes[mais_velho][0]}\nClassificação OMS: {nomes[mais_velho][3]}')
