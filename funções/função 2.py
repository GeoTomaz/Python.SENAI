estacao = input("digite se é verão ou inverno ")
temperatura = int(input("digite a temperatura "))
umidade = int(input("digite a umidade ideal "))

def qualidade_ar(estacao, temperatura, umidade):
    if estacao == "inverno":
        if temperatura >= 20 and temperatura <= 22 and umidade >= 40 and umidade <= 55:
            print(temperatura, "e", umidade, "é a qualidade ideal do ar para a estação", estacao)
        else:
            print("essa qualidade de ar não é ideal para a estação do ", estacao)
    elif estacao == "verao":
        if temperatura >= 23 and temperatura <= 26 and umidade >= 40 and umidade <= 65:
            print(temperatura, "e", umidade, "é a qualidade ideal do ar para a estação", estacao)
        else:
            print("essa qualidade de ar não é ideal para a estação do ", estacao)

qualidade_ar(estacao, temperatura, umidade)