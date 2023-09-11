valor = float(input())
saldo_atual = 0
if valor > 0:
    #TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
    saldo_atual += valor
    print(f'Deposito realizado com sucesso! Saldo atual: R$ {saldo_atual}')
elif valor == 0:
    #TODO: Imprimir a mensagem de valor inválido.
    print('Encerrando o programa...')
else:
    #TODO: Imprimir a mensagem de encerrar o programa.
    print('Valor invalido! Digite um valor maior que zero.')