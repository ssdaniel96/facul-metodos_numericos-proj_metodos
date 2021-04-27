from ..domain.gauss import Gauss
from ..data.matrizFileReader import MatrizFileReader
from ..data.matrizMaker import MatrizMaker
from ..helper.matrizHelper import MatrizHelper


class GaussController:
    matriz: list = []
    N: int
    g: Gauss

    def __init__(self):
        self.main()

    @staticmethod
    def imprimir_raizes(raizes: dict):
        print('\nImprimindo raizes...')
        for raiz in reversed(raizes):
            print(f'{raiz} = {raizes[raiz]:.4f}')

    @staticmethod
    def perguntar_de_execucao():
        print('Que forma deseja executar?')
        print('1 - Ler a matriz do arquivo matriz.txt')
        print('2 - Preencher a matriz manualmente')
        return GaussController.__resposta_de_execucao()

    @staticmethod
    def __resposta_de_execucao():
        try:
            option = int(input('Digite a opcao: '))
            if option < 1 or option > 2:
                raise Exception('Option deve ser 1 ou 2')
        except:
            print('Opcao invalida')
            return GaussController.__resposta_de_execucao()
        return option

    def preencher_por_arquivo(self):
        path = 'matriz.txt'
        readerMatriz = MatrizFileReader(path)
        self.matriz = readerMatriz.matriz
        self.N = readerMatriz.N

    def preencher_matriz(self):
        matrizMaker = MatrizMaker()
        self.matriz = matrizMaker.popular_matriz()

    def main(self):
        if (self.perguntar_de_execucao() == 1):
            self.preencher_por_arquivo()
        else:
            self.preencher_matriz()
        # self.__preencher_fake_para_test()
        self.g = Gauss(self.matriz)
        self.g.solucionar()
        MatrizHelper.imprimir_matriz(self.g.matriz_inicial, 'Matriz inicial')
        MatrizHelper.imprimir_matriz(self.g.matriz, 'Matriz escalonada')
        MatrizHelper.imprimir_matriz(self.g.raizes)
