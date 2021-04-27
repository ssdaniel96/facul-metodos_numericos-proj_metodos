from copy import deepcopy

class Gauss:
    N: int
    matriz_inicial: list = []
    matriz: list = []
    raizes: dict = dict()

    def __init__(self, matriz: list):
        self.N = len(matriz)
        self.matriz = matriz
        self.matriz_inicial = deepcopy(self.matriz)

    def __solucionar_passo(self, coluna):
        # sempre será a próxima linha após a diagonal principal que envolve a coluna
        linha_inicial = coluna+1
        # sempre a diagonal principal da coluna a ser zerada
        elemento_pivo = self.matriz[coluna][coluna]
        for i in range(linha_inicial, self.N):
            fator_multiplicacao = self.matriz[i][coluna] / elemento_pivo
            for j in range(coluna, self.N+1):
                self.matriz[i][j] = self.matriz[i][j] - \
                    fator_multiplicacao*self.matriz[coluna][j]

    def solucionar(self):
        print('Escalonando matriz...')
        passo_total_index = self.N-1  # O index maximo será a quantidade de repetições
        for passo_atual_index in range(passo_total_index):
            self.__solucionar_passo(passo_atual_index)
        self.definir_raizes()

    def definir_raizes(self):
        print('Definindo raizes...')
        representative_letter = 'X'
        for itens in reversed(self.matriz):
            indexOfdivisor = -(len(self.raizes) + 2)
            indexOfindependete = -1
            independente = itens[indexOfindependete]
            divisor = itens[indexOfdivisor]
            somaDosValores = 0
            for i in range(len(self.raizes)):
                somaDosValores += itens[-(i+2)] * \
                    self.raizes[f'{representative_letter}{self.N-i}']
            somaDosValores = independente - somaDosValores
            raiz = somaDosValores/divisor
            self.raizes[f'{representative_letter}{self.N-len(self.raizes)}'] = raiz
