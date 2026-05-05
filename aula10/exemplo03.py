print('=== Cálculo de Produtividade ===')

try:
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input('Total de Funcionários: '))
    media_por_funcionario = total_produzido / funcionarios
# TUDO O QUE PODE DAR ERRO ESTÁ AQUI EM CIMA, O RESTANTE VAI PARA O ELSE LÁ EM BAIXO

except (ValueError, TypeError):
    print('Informe um número válido. ')
except ZeroDivisionError:
    print('Informe um número válido de Funcionários.')
else:
    print(f'Média por funcionário: {media_por_funcionario:.2f}')
