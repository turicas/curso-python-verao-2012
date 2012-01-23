def fizzbuzz(numero):
    multiplo_de_3 = numero % 3 == 0
    multiplo_de_5 = numero % 5 == 0
    if multiplo_de_3 and multiplo_de_5:
        return 'fizzbuzz'
    elif multiplo_de_5:
        return 'buzz'
    elif multiplo_de_3:
        return 'fizz'    
              
    else:       
        return str(numero)
