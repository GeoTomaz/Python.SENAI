#1 - descobrir quanto custa o combústivel para encher o tanque do carro
#2 - quanto precisa de combústivel para completar 50 litros
#3 -
#passo a passo
# 1 - conseguir quantos litros falta
# 2 - multiplicar o quanto de litros que falta por 5,80
# 3 - exibir o resultado

num = 50
menos = num - 20
subtraçao = menos * 5.80
print("vai custar ", subtraçao)

capacidade_litros = int(input("digite a capacidade de litros "))
litros_tanque = int(input("digite quantos litros tem no tanque "))
preço_combustivel = int(input("digite quanto custa o preço do combustivel "))
quanto_falta = capacidade_litros - litros_tanque
valor_total = quanto_falta * preço_combustivel
print("o valor do combustivel é ", valor_total)

