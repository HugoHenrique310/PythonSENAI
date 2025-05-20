num = int (input("Adicione um número para iniciar a contagem "))
n = 0
quanti = 0
while n <= num:
    if n % 2 == 0:
        print(n)
        quanti += 1
    n = n + 1
print("A quantidade de números pares até o número solicitado é" , quanti)        