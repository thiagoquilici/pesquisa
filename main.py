# lista de 15 nomes
nomes = ['Thiago', 'Isabelly', 'Matheus', 'Pâmela', 'Camilla', 'Márcia', 'Marino', 'Marina', 'Maristela', 'Douglas', 'Marcos', 'Helena', 'Eva', 'Andrea', 'Ricardo']

# usuário informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado: ').capitalize()

# retorna o índice do nome pesquisado
#indice = nomes.index(nome)

# verifica se nome está na lista ou não (dessa forma da erro ao pesquisar um nome errado com a letra minúscula)
#if nome in nomes:
#    print(f'Nome encontrado: {nome} no índice {indice}.')
#else:
#    print(f'{nome} não encontrado na lista.')


# verifica se nome está na lista ou não e retorna o índice do nome pesquisado
try:
    indice = nomes.index(nome)
    print(f'Nome encontrado: {nome} no índice {indice}.')
except:
    print(f'{nome} não encontrado na lista.')