quantia_inicial = float(raw_input('Qual a quantia inicial? '))
quantia_mensal = float(raw_input('Qual a quantia mensal? '))
meses = int(raw_input('Quantos meses? '))
taxa = float(raw_input('Qual a taxa mensal? (em %) '))

multiplicador_mensal = 1 + (taxa / 100)
montante = quantia_inicial

nome_meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho',
              'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

print '+-----------+--------------+'
print '|    Mes    |   Montante   |'
print '+-----------+--------------+'
for mes in range(meses):
    mes_formatado = nome_meses[mes].ljust(9)
    montante_formatado = 'R$ {:8,.2f}'.format(montante)
    montante_formatado = montante_formatado.replace(',', '|').replace('.', ',')
    montante_formatado = montante_formatado.replace('|', '.')
    print '| {} | {} |'.format(mes_formatado, montante_formatado.rjust(12))
    montante = montante * multiplicador_mensal
    montante += quantia_mensal
print '+-----------+--------------+'
