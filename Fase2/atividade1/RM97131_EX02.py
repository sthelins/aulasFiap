#Sthefany Lins de Albuquerque

#entrada - quantidade de votos de cada dia da semana
#calculo - qual o mais votado
#saída - o mais votado

print("Informe o número de votos que cada dia recebeu")
segunda = int(input("Segunda "))
terca = int(input("Terça "))
quarta = int(input("Quarta "))
quinta = int(input("Quinta "))
sexta = int(input("Sexta "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O vencedor foi Segunda-feira")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("O vencedor foi Terça-feira")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("O vencedor foi Quarta-feira")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("O vencedor foi Quinta-feira")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("O vencedor foi Sexta-feira")
else:
    print("O programa não trabalha com empates, por favor refaça a votação")