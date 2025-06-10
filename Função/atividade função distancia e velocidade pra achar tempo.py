# Faça uma função que receba uma distancia em km e uma velocidade, calcule quanto tempo levará para fazer esse percurso?
distancia = int(input("Digite a distancia em Km "))
velocidade = int(input("Digite a velocidade "))

def verifica_tempo( distancia, velocidade ):
    calcula_tempo = distancia / velocidade
    print(calcula_tempo , "horas")
verifica_tempo( distancia, velocidade )




    