def calculo_imc (peso,altura):
    return peso / (altura* altura)

def resultado(imc):
    print("O resultado do imc é de {:.2f}".format(imc))


def tabela_imc(imc):
    resultado(imc)
    if imc < 18.5:
        print("Abaixo do peso")
    
    elif imc >= 18.5 and imc <= 24.9:
        print("Peso normal")

    elif  imc >= 25 and  imc <= 29.9:
        print("Sobrepeso")

    elif  imc >= 30 and  imc <= 34.9:
        print("Obesidade")

    elif  imc >= 35 and  imc <= 39.9:
        print("Obesidade grau 2")

    else:
        print(" Obesidade grau 3")

altura = float(input("Digite sua altura"))
peso = float(input("Digite seu peso: "))
imc = calculo_imc(peso,altura)
resultado(imc)