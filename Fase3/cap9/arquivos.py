arquivo = open("C:\\Users\\Sthefany\\texto.txt")

#print(arquivo)

#acessar o tudo conteudo do arquivo
#print(arquivo.read())

#acessar *uma* linha
#print(arquivo.readline())

#lista onde cada item é uma linha do arquivo
#print(arquivo.readlines())

for linha in arquivo.readlines():
    print(linha)

#fechar arquivo
#quando abre está fechando aos olhos do sistema operacional, ent assim que acabar de usar tem q fexar
arquivo.close()

#indicar para o python qual tipo de codificação que ele deve usar
#arquivo = open("C:\\Users\\Sthefany\\texto.txt", encoding="UTF-8")