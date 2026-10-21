def is_armstrong_number(number):
    numero = list(str(number))
    suma=0
    for digito in numero:
        suma+=(int(digito))**(len(numero))

    return number == suma
