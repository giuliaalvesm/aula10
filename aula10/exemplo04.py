print('\nCálculo de Produtividade')

for i in range (5):
    try:
        total_produzido = float(input('\nValor total da venda: '))
        funcionarios = int(input('Total de Funcionários: '))
        media_por_funcionario = total_produzido / funcionarios

    except (ValueError, TypeError):
        print('\nInforme um número válido. ')
    except ZeroDivisionError:
        print('\nInforme um número válido de Funcionários.')
    except KeyboardInterrupt: #pra quando eu dar ctrl+c e encerrar a operação
        print('Operação Encerrada pelo Usuário.')

#SE NÃO DER ERRO, EXECUTA O ELSE
    else:
        print(f'Média por funcionário: {media_por_funcionario:.2f}')
    finally: #obriga o bloco de código a ser executado se der erro ou não.
        print('\nPrograma Encerrado.')