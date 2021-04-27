from ..domain.gaussSiedel import GaussSiedel
from ..controllers.gaussController import GaussController
from ..data.matrizFileReader import MatrizFileReader
from ..data.matrizMaker import MatrizMaker
from ..helper.valueHelper import ValueHelper
from ..helper.matrizHelper import MatrizHelper

class GaussSiedelController:
    matriz_a: list = []
    matriz_b: list = []
    erro_aceitavel: float = 0
    n: int = 0

    def __init__(self):
        self.main()

    def __preencher_matriz_por_arquivo(self):
        self.matriz_a = MatrizFileReader('matriz.txt').matriz
        self.n = len(self.matriz_a)
        self.__preencher_erro_aceitavel()
        self.__preencher_aproximacoes_iniciais()


    def __preencher_matriz(self):
        self.__preencher_matriz_e_ordem()
        self.__preencher_erro_aceitavel()
        self.__preencher_aproximacoes_iniciais()


    def __preencher_matriz_e_ordem(self):
        mk = MatrizMaker()
        mk.popular_matriz()
        self.matriz_a = mk.matriz
        self.n = mk.N

    def __preencher_aproximacoes_iniciais(self):
        print('Vamos preencher os erros inicias: ')
        for i in range(self.n):
            value = ValueHelper.get(float, f'X{i+1}: ')
            self.matriz_b.append([value])
    
    def __preencher_erro_aceitavel(self):
        self.erro_aceitavel = ValueHelper.get(float, 'Digite o erro aceitável: ')

    
    @staticmethod
    def __imprimir_aproximacoes_com_erros(matriz: list, erros_absolutos: list, erros_relativos: list):
        print('N\t', end='')
        for i in range(len(matriz)):
            print(f'X{i+1}\t\t', end='')
        print('EA\t\tER')

        
        for i in range(len(matriz[0])):
            print(f'{i+1}\t',end='')
            for j in range(len(matriz)):
                print(f'{matriz[j][i]:.4f}\t\t', end='')
            if (i != 0):
                print(f'{erros_absolutos[i-1]:.4f}\t\t{erros_relativos[i-1]:.4f}', end='')
            print()

            
    def main(self):
        if (GaussController.perguntar_de_execucao() == 1):
            self.__preencher_matriz_por_arquivo()
        else:
            self.__preencher_matriz()

        gaussSiedel = GaussSiedel(self.matriz_a, self.matriz_b, self.erro_aceitavel)
        gaussSiedel.executar_solucao()
        MatrizHelper.imprimir_matriz(self.matriz_a, 'Matriz')
        self.__imprimir_aproximacoes_com_erros(gaussSiedel.matriz_b, gaussSiedel.erros_absolutos, gaussSiedel.erros_relativos)
        

    
