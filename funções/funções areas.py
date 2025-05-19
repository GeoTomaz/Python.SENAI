def a_circulo(raio) :
    return 3.14 * raio **2
   
def a_quadrado(numero1) :
    return numero1 * numero1
   
def a_retangulo(numero1, numero2) :
    return numero1 * numero2

def a_triangulo(lado):
    return lado **2 * round(3 ** 0.5) / 4

def a_hexágono(lado):
    return 6 * a_triangulo(lado)
   
def menu_area():
    print("[1] circulo")
    print("[2] quadrado")
    print("[3] retângulo")
    print("[4] triângulo")
    print("[5] hexágono")
    opçao = int(input("escolha uma opçao: "))
   
    if opçao == 1:
        raio = float(input("digite o raio do circulo: "))
        print("área do circulo = ", a_circulo(raio))
       
    elif opçao == 2 :
        lado = float(input("digite o lado do quadrado: "))
        print("área do quadrado = ", a_quadrado(lado))
       
    elif opçao == 3 :
        base = float(input("digite a base do retangulo: "))
        altura = float(input("digite a altura do retangulo"))
        print("área do retângulo = ", a_retangulo(base, altura))
    
    elif opçao == 4:
        base = float(input("digite a base do triangulo "))
        altura = float(input("digite a altura do triangulo "))
        print("área do triangulo é ", a_triangulo(base, altura))
        
    elif opçao == 5:
        lado = float(input("escreva um número do lado do hexágono "))
        print("a área do hexagono é ", a_hexágono(lado))
        
       
def p_circulo(raio) :
    return 3.14 **2 * raio
   
def p_quadrado(numero1) :
    return numero1 * 4
   
def p_retangulo(numero1, numero2) :
    return numero1 + numero1 + numero2 + numero2

def p_triangulo(lado):
    return lado * 3

def p_hexágono(lado):
    return lado * 6
   
def menu_perimetro():
    print("[1] circulo")
    print("[2] quadrado")
    print("[3] retângulo")
    print("[4] triângulo")
    print("[5] hexágono")
    opçao = int(input("escolha uma opçao: "))
   
    if opçao == 1:
        raio = float(input("digite o raio do circulo: "))
        print("perimetro do circulo = ", p_circulo(raio))
       
    elif opçao == 2 :
        lado = float(input("digite o lado do quadrado: "))
        print("perimetro do quadrado = ", p_quadrado(lado))
       
    elif opçao == 3 :
        base = float(input("digite a base do retangulo: "))
        altura = float(input("digite a altura do retangulo"))
        print("perimetro do retângulo = ", p_retangulo(base, altura))
    
    elif opçao == 4:
        base = float(input("digite a base do triangulo "))
        altura = float(input("digite a altura do triangulo "))
        print("perimetro do triangulo é ", p_triangulo(base, altura))
        
    elif opçao == 5:
        lado = float(input("escreva um número do lado do hexágono "))
        print("perimetro do hexagono é ", p_hexágono(lado))
       
escolha = input("escolha se voce quer area ou perimetro ")

if escolha == "area":
    menu_area()
else:
    menu_perimetro()
        