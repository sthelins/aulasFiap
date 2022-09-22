#Jogador deve digitar um número e o programa dizer se está dentro da sequencia fibonnaci ou não
#sequencia: inicia em 1 e cada novo elemento da sequencia é a soma dos dois anteriores

numeroUsuario = int(input("Informe um número inteiro "))

anterior1 = 1
anterior2 = 0

for nElemnto in range(1, numeroUsuario + 2, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    if numeroUsuario == atual:
        print("Ação bem sucedida!")
        break
    elif numeroUsuario < atual:
        print("Ação falhou")
        break
