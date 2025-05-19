import inputs

def soma(num1, num2):
    return num1 + num2
def subtração(num1, num2):
    return num1 - num2
def multiplicação(num1, num2):
    return num1 * num2
def divisão(num1, num2):
    return num1 / num2

def exibir(num1, num2):
    print("soma ", soma(num1, num2))
    print("subtração", subtração(num1, num2))
    print("multiplicação", multiplicação(num1, num2))
    print("divisão ", divisão(num1, num2))


def menu_calculadora():
    print("escolha uma opção ")
    print("1 - soma ")
    print("2 - subtração ")
    print("3 - multiplicação ")
    print("4 - divisão ")
    print("5 - todas as opções ")
    print("6 - sair ")

    while True:
        opção = inputs.input_int("escolha uma opção")
        if opção >= 1 and opção <= 6:
           print("")
        else:
            print("número invalido ")
            
        if opção != 6:
            
            num1 = inputs.input_int("digite um número ")
                
            num2 = inputs.input_int("digite outro número ")

        if opção == 1:
            print("soma ", soma(num1, num2))
            
        elif opção == 2:
            print("subtração ", subtração(num1, num2))
                                   
        elif opção == 3:
            print("multiplicação ", multiplicação(num1, num2))
                                    
        elif opção == 4:
            print("divisão ", divisão(num1, num2))
                                
        elif opção == 5:
            exibir(num1, num2)
            
        elif opção == 6:
            print("saindo... ")
            break
           
menu_calculadora()