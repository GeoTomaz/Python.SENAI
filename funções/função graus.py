def ceulsius_fahrenheit(graus_celsius):
    return graus_celsius * 1.8 + 32

def ceulsius_kelvin(graus_celsius):
    return graus_celsius + 273

celsius = int(input("digite a quantidade de graus celsius "))

print(ceulsius_fahrenheit(celsius))
print(ceulsius_kelvin(celsius))



