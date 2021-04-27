class MatrizMaker:
    N: int
    matriz: list = []

    def __preencher_ordem_sistema(self):
        try:
            self.N = int(input('Ordem do sistema: '))
        except:
            print('Ocorreu um erro, tente novamente.')
            self.__preencher_ordem_sistema()
        return self.N

    def __imprimir_explicacao(self):
        print()
        print('Instruções gerais: ')
        print('1. Digite toda a equação com espaçamentos')
        print('2. Não esqueça de incluir a variavel independente')
        print(
            'Por exemplo: \nSe a função for 23x1 + 24x2 - 2x3 = 4, inclua como 23 24 -2 4\n')

    def __popular_linha(self, N: int):
        try:
            line = input(f'Digite a {N+1}st. linha: ')
            line = self.__formatar_linha_matriz(line)
            line = [float(i) for i in line]
        except Exception as e:
            print(f'Ocorreu um erro\n{str(e)}')
            return self.__popular_linha(N)
        return line

    def __popular_matriz(self):
        for i in range(self.N):
            line = self.__popular_linha(i)
            self.matriz.append(line)

    def popular_matriz(self):
        self.__imprimir_explicacao()
        self.__preencher_ordem_sistema()
        self.__popular_matriz()
        return self.matriz

    def __formatar_linha_matriz(self, line: str):
        variaveis = line.split(' ')
        self.__verificar_irregularidades(variaveis)
        return variaveis

    def __verificar_irregularidades(self, line: list):
        tam_necessario = self.N + 1
        tam_total_variaveis = len(line)
        if tam_total_variaveis != tam_necessario:
            raise Exception(
                f'O total de variáveis com termo independete por linha deve ser: {tam_necessario}, o total informado foi: {tam_total_variaveis}')