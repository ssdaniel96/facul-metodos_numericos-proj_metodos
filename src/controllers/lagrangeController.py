from ..helper.valueHelper import criar_lista, pegar_valor
from ..domain.lagrange import Lagrange
from colorama import Fore
from colorama import Style

class LagrangeController:
    k_degree: int
    x_point: float
    x_list: list = []
    y_list: list = []

    def __init__(self):
        self.__main()

    def __main(self):
        self.__preencher_grau_e_listas()
        self.__preencher_ponto_x()
        lagrange = Lagrange(self.x_list, self.y_list, self.x_point)
        lagrange.calcular_y()
        print(f'f({lagrange.x_point}) = {lagrange.y_point:.4f}')

    def __preencher_grau_e_listas(self):
        self.__preencher_grau()
        self.__prencher_listas_x_y()

    def __preencher_ponto_x(self):
        self.x_point = pegar_valor(float, 'Digite o valor para o ponto X: ')

    def __preencher_grau(self):
        self.k_degree = pegar_valor(int, 'Digite o grau: ')

    def __prencher_listas_x_y(self):
        print('Vamos preencher agora as listas')
        print(f'Preencha sequencialmente e {Fore.YELLOW}separado por espaço TODOS os valores{Style.RESET_ALL} da lista solicitada (x ou y)')
        self.x_list = criar_lista(float, self.k_degree+1, ' ', 'Valores de X: ')
        self.y_list = criar_lista(float, self.k_degree+1, ' ', 'Valores de Y: ')
    
