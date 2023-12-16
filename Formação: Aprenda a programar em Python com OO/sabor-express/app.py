# utilizando uma biblioteca
import os

# definindo uma lista de restaurantes
restaturantes = ['Pizza', 'Sushi']

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
    print('3. Ativar restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção invalida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    # os.system('cls')
    os.system('clear')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome que deseja cadastrar: ')
    restaturantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():

    exibir_subtitulo('Listando os restaurantes')

    for restaurante in restaturantes:
        print(f'.{restaurante}')

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
                print('Ativar restaurante')
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