class gaussSiedel:

    matriz_a: list = []
    matriz_b: list = []
    erros_absolutos: list = []
    erros_relativos: list = []
    n: int = 0
    erro_aceitavel: float = 0

    def __init__(self, matriz_a: list, matriz_b: list, erro_aceitavel: float):
        self.matriz_a = matriz_a
        self.matriz_b = matriz_b
        self.n = len(matriz_a)
        self.erro_aceitavel = erro_aceitavel

    def __init__(self):
        self.__popular_teste()

    def __popular_teste(self):
        self.matriz_a = [
            [10, 5, -1, 1, 2],
            [2, 10, -2, -1, -26],
            [-1, -2, 10, 2, 20],
            [1, 3, 2, 10, -25]
        ]
        self.matriz_b = [
            [0.2],
            [-2.6],
            [2],
            [-2.5]
        ]
        self.n = 4
        self.erro_aceitavel = 10**(-4)

    def __calcular_erro_absoluto(self):
        sum_list: list = []
        for item in self.matriz_b:
            sum_item = abs(item[-1] - item[-2])
            sum_list.append(sum_item)
        max_error = max(sum_list)
        self.erros_absolutos.append(max_error)

    def __ultimo_maior_valor_matriz_b(self):
        ultimos_valores: list = []
        for valor in self.matriz_b:
            ultimos_valores.append(abs(valor[-1]))
        return max(ultimos_valores)
        

    def __calcular_erro_relativo(self):
        maior_valor = self.__ultimo_maior_valor_matriz_b()
        erro_relativo = self.erros_absolutos[-1] / maior_valor
        self.erros_relativos.append(erro_relativo)

    def adicionar_valores(self, valores: list):
        for i, valor in enumerate(valores, 0):
            self.matriz_b[i].append(valor)

    def executar_solucao(self):
        novos_valores: list = []
        for i in range(self.n):
            novo_valor = self.__executar_passo(i)
            novos_valores.append(novo_valor)
        self.adicionar_valores(novos_valores)
        self.__calcular_erro_absoluto()
        self.__calcular_erro_relativo()

        if not self.erro_aceitavel > self.erros_relativos[-1]:
            self.executar_solucao()

    def __executar_passo(self, linha: int):
        independente = self.matriz_a[linha][-1]
        divisor = self.matriz_a[linha][linha]
        soma: float = independente
        for i in range(self.n):
            if (i == linha):
                continue
            soma -= self.matriz_a[linha][i]*self.matriz_b[i][-1]
        return soma / divisor