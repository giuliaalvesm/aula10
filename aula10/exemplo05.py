print('\nCálculo de Produtividade')

for i in range (5):
    try:
        total_produzido = float(input('\nValor total da venda: '))
        funcionarios = int(input('Total de Funcionários: '))
        media_por_funcionario = total_produzido / funcionarios

    except Exception as e:
        print(f'Ops! Erro nos valores de entrada: {e}')
    except KeyboardInterrupt:
        print('Operação Encerrada pelo Usuário.')

    else:
        print(f'Média por funcionário: {media_por_funcionario:.2f}')
    finally:
        print('\nPrograma Encerrado.')