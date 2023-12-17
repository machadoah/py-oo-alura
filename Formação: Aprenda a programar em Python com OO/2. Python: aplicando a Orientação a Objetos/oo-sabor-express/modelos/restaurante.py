from modelos.avaliacao import Avaliacao

# definindo uma classe em Python
class Restaurante:

    restaurantes = []

    # self! semelhante ao this, referencia atual!
    # Construtor!
    def __init__(self, nome, categoria):
        # _ antes define que ele é private
        self._nome = nome.title() # torna a 1ª letra maiuscula!
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    # toString
    def __str__(self):
        # ou seja, não será retornado o endereço de memória e sim o nome!
        # como o toString em Java ☕
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(25)} | {str(self.media_avaliacao).ljust(25)} | {self.ativo}'
    
    #define um metodo pertencente a classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        print('-' * 25 * 3)

        for restaurante in cls.restaurantes:
            print(restaurante)

    # modifica como o atributo é lido
    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        
        return round((sum(avaliacao._nota for avaliacao in self._avaliacao) / len(self._avaliacao)), 1)