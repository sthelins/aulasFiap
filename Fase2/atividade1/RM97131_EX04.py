#Sthefany Lins de Albuquerque

#entrada - minutos atuais
#saída - LIBERDADE + o fatorial dos minutos

min = int(input("Informe o minuto atual:  "))
multiplicacao = 1

for fatorial in range(min, 0, -1):
    multiplicacao = multiplicacao * fatorial

print(f"A senha necessária para o desbloqueio é: LIBERDADE{multiplicacao}")