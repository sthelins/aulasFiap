import json

contatos = {
    "Clark Kent": {
        "Celular":"123456",
        "Email":"super@krypton.com"
    },
    "Bruce Wayne": {
        "Celular":"654321",
        "Email":"bat@caverna.com"
    }
}

#print(json.dumps(contatos, indent=4))

arquivo = open("C:\\Users\\Sthefany\\codigoFiap\\Fase3\\cap9\\dicionario.json", "w", encoding="UTF-8")
conteudo = json.dumps(contatos, indent=4)
arquivo.write(conteudo)
arquivo.close()