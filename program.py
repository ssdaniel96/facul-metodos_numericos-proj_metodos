from src.controllers.gaussController import GaussController
from src.controllers.gaussSiedelController import GaussSiedelController
from src.controllers.lagrangeController import LagrangeController
from src.helper.valueHelper import pegar_valor_entre_limites
from src.helper.consoleHelper import limpar_console

def cabecalho():
    print('Olá, seja bem-vindo a um script de execução de algoritmo de Escalonamento de Gauss')
    print('Este script foi elaborado por Daniel Soares, https://github.com/ssdaniel96')
    print('UNASP-HT, 2021, Engenharia da Computação, Métodos Numéricos Computacionais, sob orientação da Profª. Thais Michelli\n')

def escolher_metodo():
    print('1. Gauss\n2. Gauss Siedel\n3. Lagrange')
    return pegar_valor_entre_limites(int, 1, 3, 'Digite a opção: ')
    
def chamar_metodo():
    escolha = escolher_metodo()
    limpar_console()

    if (escolha == 1):
        GaussController()
    elif (escolha == 2):
        GaussSiedelController()
    elif (escolha == 3):
        LagrangeController()
    else:
        print('Valor não existe, encerrando...')
        
def main():
    cabecalho()
    chamar_metodo()

if __name__ == '__main__':
    main()

