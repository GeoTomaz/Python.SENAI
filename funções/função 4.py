peso = float(input("digite o peso em kilos"))
distancia = float(input("digite a distancia em km "))
taxa_fixa = int(input("digite a taxa fixa "))

def valor_frete(peso, distancia, taxa_fixa):
    valor = (peso * 0.5) + (distancia * 0.1) + taxa_fixa
    print("o valor do frete será:", valor, "R$ ")
    
valor_frete(peso, distancia, taxa_fixa)