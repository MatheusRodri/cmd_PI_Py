unidade_inicial = input("Informe a unidade inicial da conversão")
valor_unidade_inicial = input(f"o valor em {unidade_inicial} ")

def pesToMetros(medida):
    novo_valor = float(medida) * 0.3048
    print(f"{medida}pés em metros é {novo_valor}")

def metrosToPes(medida):
    novo_valor = float(medida) * 3.281
    print(f"{medida} metros em pés é {novo_valor}")

if(unidade_inicial == 'metros'):
    metrosToPes(valor_unidade_inicial)
else:
    pesToMetros(valor_unidade_inicial)
