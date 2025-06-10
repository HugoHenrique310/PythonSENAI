# crie uma função que calcula o valor do frete da seguinte forma:
# valor = (peso x 0.5) + (distancia x 0.1) + taxa_fixa
peso = float(input("Digite o valor do peso "))
distancia = int(input("Digite a distancia "))
taxa_fixa = float(input("Digite a taxa fixa "))

def calculo_frete (peso , distancia, taxa_fixa ):
    valor = (peso * 0.5) + (distancia * 0.1) + taxa_fixa
    resultado = valor
    print(resultado)
calculo_frete (peso , distancia, taxa_fixa )