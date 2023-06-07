class Bicicleta:
    #(__init__)defini como metodo construtor
    #(self) obrigatório ser o primerio argumento a ser definido em um metodo
    #(self) instancia o objeto
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Trim trim...')

    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada!')

    def correr(self):
        print('Pedalando!')
        print('Vrummmm...')

    #representação do objeto. exibir os valores dos atributos
    #utiliza o metodo (__str__(self) retorna qualquer valor string )
    def __str__(self):
        #primeiramente chama a instancia do obejto, que contem um atributo que consegue pegar
        #a classe e existe outro atributo que é o name
        #e chamo todos os atributos usando o (__dict__) dentro de um for
        #se a classe mudar os atributos, isss será alterado automaticamente
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    #remove todas as instancias da classe. é executado ao final ou quando você chama
    #em um determinado ponto a palavra reservada ( del + nome do objeto)
    def __del__(self):
        print('Removendo a instância b1 da classe!')

        
b1 = Bicicleta('Verde', 'Caloi', 2022, 600)

b1.buzinar()
b1.correr()
b1.buzinar()
b1.parar()

print('Representação do objeto')
print(b1)