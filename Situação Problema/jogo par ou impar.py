import random
print("olá jogador ")
print("bem vindo ao jogo par ou impar ")
print("escolha uma das opções abaixo ")
print("e continue o jogo ")
print("sua oponente é a maquina, vença ela ")
print("boa sorte ")

while True:
    print("menu jogo ")
    print("[1] - impar ")
    print("[2] - par ")
    print("[3] - sair ")
   
    num = int(input("escolha um número para começarmos o jogo: "))
    if num == 1:
        print("você é impar ")
        num1 = int(input("escolha um número de 1 a 10: "))
    elif num == 2:
        print("você é par ")
        num1 = int(input("escolha um número de 1 a 10: "))
    elif num == 3:
        break
    n_aleatorio = random.randint(1,10)

    print("A maquina escolheu:", n_aleatorio)
    soma = n_aleatorio + num1
    print("o resultado é ", soma)
    
    
    if soma % 2 == 0:
        
        if num == 1:
            print("o jogador perdeu ")
        else:
            print("o jogador venceu ")
 
    else:
        print("")
        
        if num == 2:
            print("o jogador perdeu ")
            
        else:
            print("o jogador venceu ")
          
      
            
    
    
    
           
       
