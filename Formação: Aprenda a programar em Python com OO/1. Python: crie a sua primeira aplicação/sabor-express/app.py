# utilizando uma biblioteca
import os

# definindo um dicionario que armazene os restaurantes
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]

def exbir_nome_do_programa():
     # exibe nome do app
     # https://fsymbols.com/pt/letras/
      print("""
      𝒔𝒂𝒃𝒐𝒓 𝒆𝒙𝒑𝒓𝒆𝒔𝒔
      """)

def voltar_ao_menu_principal():
    input('\nDigite alguma tecla para voltar ao menu peincipal: ')
    main()

def exbir_opcoes():
    # opções para serem utilizadas
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção invalida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    # os.system('cls')
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Docstring: 
    
    Essa função é responsavel por cadastrar um novo restaurante
    
    Inputs: 
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():

    exibir_subtitulo('Listando os restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')

    for restaurante in restaurantes:

        if restaurante['ativo'] == True:

            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desayivado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do resurante')

    nome_restaurante = input('Digite o nome do resurante que deseja alternar do estado: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            # print(f'Resurante {nome_restaurante} foi ativado com sucesso!')

            # operador ternário!
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucecesso'

            print(mensagem)
    
    if restaurante_encontrado == False:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')

    voltar_ao_menu_principal()

def escolher_opcao():

    # lidando com exceptions!

    try:
        # por padrão o input é string!
        opcao_escolhida = int(input('Escolha uma opção: '))

        # interpolação de string! com o 'f'
        print(f'Você escolheu a opção {opcao_escolhida} !')

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    exibir_subtitulo('Finalizando app')

# define esse codigo como principal
def main():
    os.system('clear')
    exbir_nome_do_programa()
    exbir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
        main()