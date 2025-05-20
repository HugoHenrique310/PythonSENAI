def menu_calculadora():
    while True:
        print("Menu")
        print("")
        print("1 - soma")
        print("2 - subtração")
        print("3 - multiplicação")
        print("4 - divisão")
        print("5 - todas")
        print("6 - sair")
        while True:
            try:
                escolha = int(input("Escolha um número"))
                break
            
            except ValueError:
                print("Digite somente números ex:6")
                
        if escolha != 6:
            while True:
                try:
                    num1 = float(input("Digite um número"))
                    break
                
                except ValueError:
                    print("Digite somente números ex:6")
                    
            while True:
                try:
                    num2 = float(input("Digite um número"))
                    break
                except ValueError:
                    print("Digite somente números ex:6")
                 
                 

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
        elif escolha == 6:
            print("sair")
            break
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


menu_calculadora()