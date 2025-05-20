nota1 = int(input("Digite uma nota: "))
nota2 = int(input("Digite outro nota: "))

soma = nota1 + nota2
média = soma / 2


if nota1 > 0 and nota1 <= 100 and nota2> 0 and nota2 <= 100:
    
    if média >= 70:
        print("aprovado")
    
    elif média >= 50 and média <= 70:
        print("recuperação")
    
    elif média < 50:
       print("reprovado")
  