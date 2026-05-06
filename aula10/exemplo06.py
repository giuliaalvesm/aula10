#Calcular média de notas
#Não sabemos quantos alunos, mas terão 4 notas sempre

def calcula_media(lista_notas):
    total = sum(lista_notas) #função de soma da lista
    media = total / len(lista_notas) #len é uma função usada para saber a quantidade de elementos dentro da lista
    return total, media

contador = 1
#resposta = 'S'
while True:
    print(f'\nAluno {contador}')
    aluno = input('Nome do aluno: ')

    notas = []
    try:
        for i in range(4):
            nota = float(input('Informe a nota: '))
            notas.append(nota)

    except ValueError:
        print('Erro: Valor inválido.')
    else:
        total, media = calcula_media(notas)
        print('\nRESULTADO')
        print(f'Aluno: {aluno}')
        print(f'Total de pontos: {total}')
        print(f'Média: {media:.2f}')

    finally:
        print('Processo Encerrado.')

    #Causa de parada do loop
    opcao = input('\nDeseja calcular para outro aluno? ').strip().upper()
    if opcao != 'S':
        break
    contador += 1

print('\nPrograma Encerrado.')