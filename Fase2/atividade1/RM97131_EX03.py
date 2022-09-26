#Sthefany Lins de Albuquerque

#entrada - 25 alunos número ímpar, dps 25 alunos número par
#saída - exibir média de cada uma das metades e informar qual teve maior nota
#sempre exibir msg com que aluno(impar ou par) o professor tem que digitar e qual o número do aluno

#alunos pares
somaPar = 0
mediaPar = 0
for alunosPar in range(2, 51, 2):
    notaPar = float(input(f"Você está digitando as notas do alunos pares, por favor insira a nota do aluno {alunosPar}: "))
    somaPar += notaPar

mediaPar = somaPar/25

#alunos ímpares
somaImpar = 0
mediaImpar = 0
for alunosImpar in range(1, 50, 2):
    notaImpar = float(input(f"Você está digitando as notas do alunos ímpares, por favor insira a nota do aluno {alunosImpar}: "))
    somaImpar += notaImpar

mediaImpar = somaImpar/25

# - 300 pra marge de erro
maiorMédia = - 300
if mediaPar > mediaImpar:
    maiorMédia = mediaPar
else:
    maiorMédia = mediaImpar

print(f"A média dos alunos pares foi {mediaPar} e dos alunos ímpares foi {mediaImpar}")
print(f"A maior média foi {maiorMédia}")
