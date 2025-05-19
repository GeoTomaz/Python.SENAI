#1 - quantos litros de combustivel e quantos reais preciso pra fazer uma viagem
#2 - quantos litros vc precisa pra percorrer 800 km e quanto vai ustar o combustivel
#3

#passo a passo
#1-conseguir o quantos reais e quanto de combustivel você vai gastar
#2-


viagem = 800
autonomia = 7
tanque = 10
distancia = 90
preço = 6.90

falta_km = viagem - distancia
litros = falta_km / autonomia
falta_litros = litros - tanque
valor_combustivel = falta_litros * preço
print(" o valor do combustivel é de: R$", valor_combustivel)
print("o combustivel que falta é ", falta_litros) 
