def converte_de_romanos_para_indoarabico(numero_romano):
    arabicos = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D':500,'M':1000}
    total = 0
    anterior = None
    for romano in numero_romano:
        if anterior is not None and arabicos[romano] > arabicos[anterior]:
            total += arabicos[romano] - 2 * arabicos[anterior]
        else:
            total += arabicos[romano]
        anterior = romano
    return total
