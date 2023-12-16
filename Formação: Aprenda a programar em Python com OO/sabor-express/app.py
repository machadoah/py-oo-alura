# utilizando uma biblioteca
import os

def exbir_nome_do_programa():
     # exibe nome do app
     # https://fsymbols.com/pt/letras/
      print("""
      𝒔𝒂𝒃𝒐𝒓 𝒆𝒙𝒑𝒓𝒆𝒔𝒔
      """)

"""
strings podem ser usadas com:

(' ') -> aspas simples
(" ") -> aspas duplas
"""
def exbir_opcoes():
    # opções para serem utilizadas
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def escolher_opcao():
    # por padrão o input é string!
    opcao_escolhida = int(input('Escolha uma opção: '))

    # interpolação de string! com o 'f'
    print(f'Você escolheu a opção {opcao_escolhida} !')
    
    """
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()
    """

    match opcao_escolhida:
         case 1:
              print('Cadastrar restaurante')
         case 2:
              print('Listar restaurantes')
         case 3:
              print('Ativar restaurante')
         case _:
              finalizar_app()

def finalizar_app():
    # os.system('cls') no windows
    os.system('clear')
    print('Finalizando app\n')

# define esse codigo como principal

def main():
     exbir_nome_do_programa()
     exbir_opcoes()
     escolher_opcao()

if __name__ == '__main__':
        main()