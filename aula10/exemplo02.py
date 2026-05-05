# Repetindo

for i in range (5):
    try:
        total_produzido = float(input('\nValor total da venda: '))
        funcionarios = int(input('Total de Funcionários: '))

        media_por_funcionario = total_produzido / funcionarios
        print(f'Média por funcionário: {media_por_funcionario:.2f}')
    except ValueError:
        print('\nInforme um número válido.')
    except ZeroDivisionError:
        print('\nInforme um número válido de Funcionários.')