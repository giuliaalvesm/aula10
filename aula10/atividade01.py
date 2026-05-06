print('\nCAIXA ELETRÔNICO')
print('\nSALDO DISPONÍVEL: R$1000')


try:
    saldo = 1000
    valor_saque = float(input('\nInforme o valor que deseja sacar: '))
except ValueError:
    print('\nInforme um número válido.')
except KeyboardInterrupt:
    print('\nPrograma encerrado pelo usuário.')
else:
    if valor_saque > saldo:
        print('Saldo Insuficiente')
    elif valor_saque <=2:
        print('Informe um valor maior ou igual a R$2')
    else:
        saldo -= valor_saque
        print(f'Valor selecionado: {valor_saque}')
        print('\nSaque realizado com sucesso.')
finally:
    print('\nTransação Finalizada.')
