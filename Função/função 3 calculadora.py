def menu_calculadora(num1,num2):
    print("Menu")
    print("")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - todas")
    escolha = int(input("Escolha um número"))
    if escolha == 1:
        print("O resultado da adição é" , soma(num1,num2))
    elif escolha == 2:
        print("O resultado da subtração é" , subtração(num1,num2))
    elif escolha == 3:
        print("O resultado da multiplicação é" , multiplicação(num1,num2))
    elif escolha == 4:
        print("O resultado da divisão é" , divisão(num1,num2))
    elif escolha == 5:
        resultados(num1,num2)
    
    else:
         print("invalido")
def soma(num1,num2 ):
    return num1 + num2

def subtração(num1,num2):
    return num1 - num2

def multiplicação(num1,num2):
    return num1 * num2

def divisão (num1,num2):
    return num1 / num2

def resultados(num1,num2):
    print(soma (num1,num2), "é o resultado da adição")
    print(subtração (num1,num2), "é o resultado da subtração")
    print(multiplicação (num1,num2), "é o resultado da multiplicação")
    print(divisão (num1,num2), "é o resultado da divisão")

num1 = float(input("Digite um número"))
num2 = float(input("Digite outro número"))

menu_calculadora(num1,num2)