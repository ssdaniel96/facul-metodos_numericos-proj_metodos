class MatrizHelper:
    @staticmethod
    def imprimir_matriz(matriz: [], msg: str, rep: str = 'X'):
        print('\n' + msg)
        n: int = len(matriz)
        for i in range(n):
            print(f'\t{rep}{i+1}\t', end='')
        print()
        for i in range(len(matriz)):
            print(f'L{i+1}\t', end='')
            for j in range(len(matriz[i])):
                if j != len(matriz[i])-1:
                    print(f'{matriz[i][j]:.4f}\t\t', end='')
                else:
                    print(f'=\t{matriz[i][j]:.4f}')
        print()