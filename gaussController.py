from gauss import Gauss
from matrizFileReader import MatrizFileReader
class GaussController:
    matriz: list = []
    N: int
    g: Gauss

    def __init__(self):
        self.__cabecalho()
        self.main()

    def __preencher_fake_para_test(self):
        self.matriz = [
            [10.0, 5.0, -1.0, 1.0, 2.0],
            [2.0, 10.0, -2.0, -1.0, -26.0],
            [-1.0, -2.0, 10.0, 2.0, 20.0],
            [1.0, 3.0, 2.0, 10.0, -25.0]
        ]
        self.N = 4

    def __cabecalho(self):
        print('Olá, seja bem-vindo a um script de execução de algoritmo de Escalonamento de Gauss')
        print('Este script foi elaborado por Daniel Soares, https://github.com/ssdaniel96')
        print('UNASP-HT, 2021, Engenharia da Computação, Métodos Numéricos Computacionais, sob orientação da Profª. Thais Michelli\n')
     
    def __imprimir_explicacao(self):
        print()
        print('Instruções gerais: ')
        print('1. Digite toda a equação com espaçamentos')
        print('2. Não esqueça de incluir a variavel independente')
        print('Por exemplo: \nSe a função for 23x1 + 24x2 - 2x3 = 4, inclua como 23 24 -2 4\n')

    def preencher_ordem_sistema(self):
        try: 
            self.N = int(input('Ordem do sistema: '))
        except:
            'Ocorreu um erro, tente novamente.'
            self.__preencher_ordem_sistema()

    def __popular_linha(self, N: int):
        try:
            line = input(f'Digite a {N+1}st. linha: ')
            line = self.__formatar_linha_matriz(line)
            line = [float(i) for i in line]
        except Exception as e:
            print(f'Ocorreu um erro\n{str(e)}')
            return self.__popular_linha(N)
        return line

    def popular_matriz(self):
        for i in range(self.N):
            line = self.__popular_linha(i)
            self.matriz.append(line)
    
    def __formatar_linha_matriz(self, line: str):
        variaveis = line.split(' ')
        self.__verificar_irregularidades(variaveis)
        return variaveis
    

    def __verificar_irregularidades(self, line: list):
        tam_necessario = self.N + 1
        tam_total_variaveis = len(line)
        if tam_total_variaveis != tam_necessario:
            raise Exception(f'O total de variáveis com termo independete por linha deve ser: {tam_necessario}, o total informado foi: {tam_total_variaveis}')

    def imprimir_matriz(self, matriz: [], msg: str, rep: str = 'X'):
        print('\n' + msg)
        for i in range(self.N):
            print(f'\t{rep}{i+1}', end='')
        print()
        for i in range(len(matriz)):
            print(f'L{i+1}\t', end='')
            for j in range(len(matriz[i])):
                if j != len(matriz[i])-1:
                    print(f'{matriz[i][j]:.2f}\t', end='')
                else:
                    print(f'=\t{matriz[i][j]:.2f}')

    def imprimir_raizes(self, raizes: dict):
        print('\nImprimindo raizes...')
        for raiz in reversed(raizes):
            print(f'{raiz} = {raizes[raiz]:.2f}')

    def __perguntar_de_execucao(self):
        print('Que forma deseja executar?')
        print('1 - Ler a matriz do arquivo matriz.txt')
        print('2 - Preencher a matriz manualmente')
        return self.__resposta_de_execucao()
    
    def __resposta_de_execucao(self):
        try:
            option = int(input('Digite a opcao: '))
            if option < 1 or option > 2:
                raise Exception('Option deve ser 1 ou 2')
        except:
            print('Opcao invalida')
            self.__resposta_de_execucao()
        return option

    def preencher_por_arquivo(self):
        path = 'matriz.txt'
        readerMatriz = MatrizFileReader(path)
        self.matriz = readerMatriz.matriz
        self.N = readerMatriz.N

    def main(self):
        if (self.__perguntar_de_execucao() == 1):
            self.preencher_por_arquivo()
        else:
            self.__imprimir_explicacao()
            self.preencher_ordem_sistema()
            self.popular_matriz()
        # self.__preencher_fake_para_test()
        self.g = Gauss(self.matriz)
        self.g.solucionar()
        self.imprimir_matriz(self.g.matriz_inicial, 'Matriz inicial')
        self.imprimir_matriz(self.g.matriz, 'Matriz escalonada')
        self.imprimir_raizes(self.g.raizes)

def main():
    GaussController()

if __name__ == '__main__':
    main()