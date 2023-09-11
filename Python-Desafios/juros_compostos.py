valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

#TODO: Iterar, baseado no período em anos, para calculo do valor_final com os juros.

for i in range(periodo):
    valor_final += (valor_final * taxa_juros)


print(f"Valor final do investimento: R${valor_final:.2f}")