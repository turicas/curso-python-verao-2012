quantia = float(raw_input('Qual a quantia? '))
meses = int(raw_input('Quantos meses? '))
taxa = float(raw_input('Qual a taxa mensal? (em %) '))

taxa_percentual = taxa / 100.0
taxa_total = (1 + taxa_percentual) ** meses

print 'Valor final dos rendimentos:'
print quantia * taxa_total
