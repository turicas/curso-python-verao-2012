quantia_inicial = float(raw_input('Qual a quantia inicial? '))
quantia_mensal = float(raw_input('Qual a quantia mensal? '))
meses = int(raw_input('Quantos meses? '))
taxa = float(raw_input('Qual a taxa mensal? (em %) '))

multiplicador_mensal = 1 + (taxa / 100)
montante = quantia_inicial
for mes in range(meses):
    print mes + 1, montante #imprimindo mes e montante atual
    montante = montante * multiplicador_mensal #adicionando juros
    montante += quantia_mensal #montante = montante + quantia_mensal
