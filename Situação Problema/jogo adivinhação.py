import random
print("bem vindo ao jogo de adivinhação ")
print("adivinhe o número e vença ")
print("boa sorte ")
n_aleatorio = random.randint(1,100)
while True:
    num = int(input("digite um número: "))
    if n_aleatorio > num:
        print("o número é maior que ", num)
    elif n_aleatorio < num:
        print("o número é menor que ", num)
        
    else:
        print("voce acertou ")
        print("deseja continuar o jogo? ")
        print("[1] - sim ")
        print("[2] - não ")
        escolha = int(input("escolha uma opção "))
        if escolha == 1:
            print("vamos para uma nova rodada ")
            n_aleatorio = random.randint(1,100)   
        else:
            break
    
        

    
