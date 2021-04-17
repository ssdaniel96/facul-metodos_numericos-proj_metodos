class MatrizFileReader:
    path: str
    N: int
    matriz: list = []
    def __init__(self, path: str):
        self.path = path
        self.main()

    def __definirOrdemDaMatriz(self, file):
        comment_lines_count = 0
        lines_count = 0
        for linha in file:
            linha = linha.strip()
            if linha[0] == '!':
                comment_lines_count += 1
            else:
                lines_count+=1
        file.seek(0)
        self.N = lines_count

    def __carregar_matriz(self, path: str):
        self.matriz = []
        file_matriz = open(path, 'r')
        self.__definirOrdemDaMatriz(file_matriz)
        print('Iniciando leitura da matriz...')
        for linhano, linha in enumerate(file_matriz, 1):
            linha = linha.strip()
            if not linha[0] == '!':
                print(f'{linhano} - {linha}')
                try:
                    linha = self.__preencher_linha(linha)
                    self.matriz.append(linha)
                except Exception as e:
                    print('Um erro foi encontrado.')
                    print(str(e))
                    print(f'Abra o arquivo corrija a linha {linhaNo}')
                    input('Pressione enter para continuar')
                    self.__carregar_matriz()
        file_matriz.close()
        self.N = len(self.matriz)

    def __preencher_linha(self, line: str):
        variaveis = line.split(' ')
        variaveis = [float(i) for i in variaveis]
        if len(variaveis) != self.N+1:
            raise Exception(f'O total de variáveis com termo independete por linha deve ser: {self.N+1}, o total informado foi: {len(variaveis)}')
        return variaveis

    def main(self):
        self.__carregar_matriz(self.path)
