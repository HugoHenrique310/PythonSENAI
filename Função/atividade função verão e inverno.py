# temperatura ideal para a qualidade do ar é entre 20°C 22°C no inverno e 23°C e 26°C no verão.
# umidade ideal para a saúde humana deve estar entre 40% e 55% no inverno e 40% e 65% no verão.
# Faça uma função que verifica qualidade do ar com base nesses dados.
estação_ano = str(input("Digite a estação do ano se é inverno ou verão "))
temperatura = int(input("Digite a temperatura do ar ex:(24°) "))
umidade = int(input("Digite a umidade do ar ex:(40%) "))

def verificar_qualidade_ar(estação_ano, temperatura, umidade):

    
    if estação_ano == "verão":
        if temperatura >= 23 and temperatura <= 26 and umidade >= 40 and umidade <= 65:
            print("A qualidade do ar está ideal")
        else:
            print("A qualidade do ar não está ideal ")
            
    elif estação_ano == "inverno":
        if temperatura >= 20 and temperatura <= 22 and umidade >= 40 and umidade <= 55:
            print("A qualidade do ar está ideal")
        else:
            print("A qualidade do ar não está ideal ")
                
verificar_qualidade_ar(estação_ano, temperatura, umidade)
         
        
    