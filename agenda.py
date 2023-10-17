AGENDA = {}

def mostrar_contatos():
    if len(AGENDA) > 0:
        for contato in AGENDA:
            buscar_contato(contato)
            print()
    else:
        print('>>>> Agenda vazia')
        print('                   ')
def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print('Telefone:',  AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereço'])
        print()
    except KeyError:
        print('>>>> Contato inexistente')
        print('                         ')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)
        print('                       ')

def ler_detalhes_contato():
    telefone = input('Digite o numero de telefone: ')
    email = input('Digite o email do contato: ')
    endereço = input('Digite o nome do endereço ')
    return telefone, email, endereço

def incluir_editar_contato(contato, telefone, email, endereço):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereço': endereço,
    }
    salvar()
    print()
    print(">>>> Contato {} adicionado/editado com sucesso".format(contato))
    print()

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print(">>>> Contato {} excluido com sucesso".format(contato))
        print()
    except KeyError:
        print('>>>> Contato inexistente')
        print('                         ')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu')
        print(error)
        print('                       ')

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereço = AGENDA[contato]['endereço']
                arquivo.write('{},{},{},{}\n'.format(contato, telefone, email, endereço))
        print('>>>> Agenda exportada com sucesso')
    except Exception as error:
        print('>>>> Alguma falha ocorreu ao exportar contatos')
        print(error)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
           linhas = arquivo.readlines()
           for linha in linhas:
               detalhes = linha.strip().split(',')

               nome = detalhes[0]
               telefone = detalhes[1]
               email = detalhes[2]
               endereço = detalhes[3]

               incluir_editar_contato(nome, telefone, email, endereço)
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)

def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereço = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereço': endereço,
                }
        print(">>>> Database Carregado com Sucesso")
        print(">>>> {} contatos carregados".format(len(AGENDA)))
    except FileNotFoundError:
        print('>>>> Arquivo nao encontrado')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu')
        print(error)
def imprimir_menu():
    print('1 -- Mostrar todos os contatos da agenda')
    print('2 -- Buscar contato')
    print('3 -- Incluir contato')
    print('4 -- Editar contato')
    print('5 -- Excluir contato')
    print('6 -- Exportar contatos para CSV')
    print('7 -- Importar contatos CSV')
    print('0 -- Fechar programa')

#INICIO DO PROGRAMA
carregar()
while True:
    imprimir_menu()
    opçao = input('Escolha uma opção: ')
    if opçao == '1':
        print('                     ')
        mostrar_contatos()
    elif opçao == '2':
        print('                     ')
        contato = input('Digite o nome do contato:  ')
        buscar_contato(contato)
        print('                     ')
    elif opçao == '3':
        print('                     ')
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>> Contato ja existente')
            print('                           ')
        except KeyError:
            telefone, email, endereço = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereço)
    elif opçao == '4':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>> Editando contato:', contato)
            incluir_editar_contato(contato, telefone, email, endereço)
        except KeyError:
            print('>>>> Contato inexistente')



            print('                  ')

    elif opçao == '5':
        print('                     ')
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opçao == '6':
        nome_do_arquivo = input("Digite o nome do arquivo a ser exportado:  ")
        exportar_contatos(nome_do_arquivo)
    elif opçao == '7':
        nome_do_arquivo = input("Digite o nome do arquivo a ser importado:  ")
        importar_contatos(nome_do_arquivo)
    elif opçao == '0':
        print('                     ')
        print('>>>> Fechando programa')
        break
    else:
        print('                     ')
        print('>>>> Opção invalida')
        print('                     ')

