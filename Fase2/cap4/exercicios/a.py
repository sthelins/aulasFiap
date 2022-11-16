#python

def identificarNumeroPrimo(a):
    if a % 2 == 0:
        NumeroPrimo = True
    else:
        NumeroPrimo = False
    print(NumeroPrimo)


numero = int(input("Digite um número: "))
identificarNumeroPrimo(numero)
