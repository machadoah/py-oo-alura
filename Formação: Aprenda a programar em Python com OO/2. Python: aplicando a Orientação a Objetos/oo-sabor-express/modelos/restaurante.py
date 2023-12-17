# definindo uma classe em Python
class Restaurante:

    restaurantes = []

    # self! semelhante ao this, referencia atual!
    # Construtor!
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    # toString
    def __str__(self):
        # ou seja, não será retornado o endereço de memória e sim o nome!
        # como o toString em Java ☕
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(restaurante)


restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
print(vars(restaurante_pizza))

Restaurante.listar_restaurantes()