from modelos.restaurante import Restaurante


# restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()

restaurante_mexicano.receber_avaliacao('Isa', 10)
restaurante_mexicano.receber_avaliacao('Tonio', 9)
restaurante_mexicano.receber_avaliacao('Maria Isabel', 9)

# torna main!
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()