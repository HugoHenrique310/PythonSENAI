peso = int (input("Digite o seu peso"))
altura = float(input("Digite a sua altura"))
imc1 = altura * altura
imc2 = peso / imc1 

if imc2 < 18.5:
    print("Abaixo do peso")
    
elif imc2 >= 18.5 and imc2 <= 24.9:
    print("Peso normal")

elif imc2 >= 25 and imc2 <= 29.9:
    print("Sobrepeso")

elif imc2 >= 30 and imc2 <= 34.9:
    print("Obesidade")

elif imc2 >= 35 and imc2 <= 39.9:
    print("Obesidade grau 2")

else:
    imc2 >= 60
    print(" Obesidade grau 3")