print('Bem-vindos a empresa do Alex Lopes Quintela\n')

# Variáveis:
lista_funcionarios = []
id_global = 4738781
informacoes_funcionarios = {'nome': [], 'setor': [], 'salario': [], 'id': []}
salario = 0
escolha = 0


# Funções:
def cadastrar_funcionario(id_funcionario):  # Adiciona dados do(a) funcionário(a) na lista_funcionários
    global lista_funcionarios
    global salario

    print('-' * 38 + '\n' + '-' * 4 + '|', 'MENU CADASTRAR FUNCIONÁRIO', '|' + '-' * 4)

    # Mostra o Id do funcionário
    print(f'O Id do(a) funcionário(a) vai ser: {id_funcionario}')

    # Pergunta nome:
    nome = input('Informe o nome do funcionário(a): ').capitalize()
    while not nome.isalpha():
        nome = input('Informe o nome do funcionário(a): ').capitalize()

    # Pergunta setor:
    setor = input('Em qual setor ele(a) trabalha?: ')
    while not setor:
        setor = input('Em qual setor ele(a) trabalha?: ')

    # Pergunta salário:
    while True:
        try:
            salario = float(input('Informe o salário do(a) funcionário(a): '))
        except ValueError:
            continue

        break

    # Adiciona as informações à lista:
    informacoes_funcionarios['nome'].append(nome)
    informacoes_funcionarios['setor'].append(setor)
    informacoes_funcionarios['salario'].append(salario)
    informacoes_funcionarios['id'].append(id_funcionario)

    lista_funcionarios = informacoes_funcionarios.copy()

    print(f'\nFuncionário(a) {nome} cadastrado(a) com sucesso!\n')


def consultar_funcionarios():  # Lista os funcionários já cadastrados
    global escolha

    while True:
        print('-' * 38 + '\n' + '-' * 4 + '|', 'MENU CONSULTAR FUNCIONÁRIO', '|' + '-' * 4)
        print('1. Consultar todos\n2. Consultar por Id\n3. Consultar por setor\n4. Retornar ao menu')

        # Pergunta a opção desejada:
        try:
            escolha = int(input('Digite a opção desejada: '))
            print('')
        except ValueError:
            continue

        match escolha:
            case 1:  # Consultar todos:
                if len(lista_funcionarios) == 0 or len(lista_funcionarios['nome']) == 0:
                    print('Nenhum funcionário cadastrado!\n')
                    break

                for i in range(len(lista_funcionarios['nome'])):
                    print(f'Nome: {lista_funcionarios["nome"][i]}  |  '
                          f'Setor: {lista_funcionarios["setor"][i]}  |  '
                          f'Salário: {lista_funcionarios["salario"][i]:.2f}  |  '
                          f'Id: {lista_funcionarios["id"][i]}')
                print('')

            case 2:  # Consultar por Id:
                if len(lista_funcionarios) == 0:
                    print('Nenhum funcionário cadastrado!\n')
                    break

                # Pergunta Id:
                id_funcionario = input('Digite o Id do(a) funcionário(a): ')
                while not id_funcionario.isdigit():
                    id_funcionario = input('Digite o Id do(a) funcionário(a): ')
                id_funcionario = int(id_funcionario)

                print('')
                status = False

                # Mostra as informações:
                for i in range(len(lista_funcionarios['nome'])):
                    if lista_funcionarios['id'][i] == id_funcionario:
                        print(f'Nome: {lista_funcionarios["nome"][i]}  |  '
                              f'Setor: {lista_funcionarios["setor"][i]}  |  '
                              f'Salário: {lista_funcionarios["salario"][i]:.2f}  |  '
                              f'Id: {lista_funcionarios["id"][i]}')
                        status = True
                        print('')

                if not status:
                    print('Funcionário(a) Inexistente.')

            case 3:  # Consultar por setor:
                if len(lista_funcionarios) == 0 or len(lista_funcionarios['nome']) == 0:
                    print('Nenhum funcionário cadastrado!\n')
                    break

                # Pergunta o setor:
                setor = input('Digite o setor do(s) funcionário(s): ')
                while not setor:
                    setor = input('Digite o setor do(s) funcionário(s): ')
                print('')

                # Mostra as informações:
                for i in range(len(lista_funcionarios['nome'])):
                    if lista_funcionarios['setor'][i] == setor:
                        print(f'Nome: {lista_funcionarios["nome"][i]}  |  '
                              f'Setor: {lista_funcionarios["setor"][i]}  |  '
                              f'Salário: {lista_funcionarios["salario"][i]:.2f}  |  '
                              f'Id: {lista_funcionarios["id"][i]}')
                print('')

            case 4:  # Sair:
                return

            case _:  # Qualquer outra opção
                print('Opção inválida')


def remover_funcionario():  # Remove perguntando o Id:
    print('-' * 36 + '\n' + '-' * 4 + '|', 'MENU REMOVER FUNCIONÁRIO', '|' + '-' * 4)
    while True:
        # Pergunta Id:
        id_funcionario = input('Digite o Id do funcionário: ')
        if not id_funcionario.isdigit():
            print('Id inválido\n')
            continue

        print('')
        id_funcionario = int(id_funcionario)
        status = False

        # Mostra as informações de quem vai ser removido:
        for i in range(len(lista_funcionarios['nome'])):
            if lista_funcionarios['id'][i] == id_funcionario:
                print(f'Nome: {lista_funcionarios["nome"][i]}  |  '
                      f'Setor: {lista_funcionarios["setor"][i]}  |  '
                      f'Salário: {lista_funcionarios["salario"][i]:.2f}  |  '
                      f'Id: {lista_funcionarios["id"][i]}')
                print('')

                # Remove informações da lista_funcionarios:
                del lista_funcionarios['nome'][i]
                del lista_funcionarios['setor'][i]
                del lista_funcionarios['salario'][i]
                del lista_funcionarios['id'][i]

                print('Funcionário Removido!\n')
                status = True
                break

        if not status:
            print('Id inválido!\n')
            continue

        break


# Código principal (Main):
while True:  # Menu:
    print('-' * 26 + '\n' + '-' * 4 + '|', 'MENU PRINCIPAL', '|' + '-' * 4)
    print('1) Cadastrar Funcionário\n2) Consultar Funcionário\n3) Remover Funcionário\n4) Encerrar Programa')

    # Pergunta qual opção quer usar:
    opt = input('Digite a opção desejada: ')
    while not opt.isdigit():
        opt = input('Digite a opção desejada: ')
    opt = int(opt)

    match opt:

        case 1:  # Cadastrar funcionário:
            print('')

            # Adiciona 1 ao id_global:
            id_global += 1
            cadastrar_funcionario(id_global)

        case 2:  # Consultar funcionário:
            print('')
            consultar_funcionarios()

        case 3:  # Remover funcionário:
            print('')
            remover_funcionario()

        case 4:  # Sair e fechar programa:
            print('-' * 24 + '\n' + ' ENCERRANDO PROGRAMA...')
            break

        case _:  # Qualquer outra opção:
            print('\nOpção inválida')
