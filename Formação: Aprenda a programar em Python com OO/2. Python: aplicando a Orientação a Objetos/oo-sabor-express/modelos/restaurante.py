# definindo uma classe em Python
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()

# acessando atributos dos objetos!
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]
# [<__main__.Restaurante object at 0x7f7f218d7f70>, <__main__.Restaurante object at 0x7f7f218d7f40>]
# local de memória onde esta sendo armazenado os objetos!

# a função dir, exibe todas as informações dos objetos!
# a função vars, exibe todas as informações dos objetos, em dicionario!
print(vars(restaurante_praca))


