def celsius_kelvin(temperatura_C):
    return temperatura_C + 273

def celsius_fa(temperatura_C):
    return temperatura_C * 1.8 + 32

temperatura_C = float(input ("Digite uma temperatura em graus celsius: "))


print(temperatura_C, "°C equivalem a", celsius_fa(temperatura_C), "°F e",celsius_kelvin (temperatura_C), "K")    