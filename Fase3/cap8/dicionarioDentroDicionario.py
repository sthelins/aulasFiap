contatos = {
    "Amanda Clark": {
        "celular":"123456",
        "email": "amanda@gmail.com"
    },
    "Monica Geller": {
        "celular":"987654",
        "email": "monica@gmail.com"
    }
}

print(contatos.items())

print(contatos.keys())
print(contatos.values())

for nome, formas_contatos in contatos.items():
    print(f"O contatos {nome}")
    for forma, valor in formas_contatos.items():
        print(f"pode ser contatado por {forma}: {valor}")
    print(f"\n\n")