mae = {
    "nome": "Gislaine",
    "idade": 39,
    "altura": 1.67,
    "cor": "morena"
}

pai = {
    "nome": "Sergio",
    "idade": 51,
    "altura": 1.80,
    "cor": "moreno"  
}

irma = {
    "nome": "Nicoli",
    "idade": 10,
    "altura": 1.35,
    "cor": "morena"   
}

#exibir uma lista de dicionarios
lista_familia = [mae, pai, irma]
    
    #escolhendo os campos

    
    #exibindo todos
for familia in lista_familia:
    for chave, valor in familia.items():
        print(f"{chave} - {valor}")
    print()
    
    