from src.controllers.gaussController import GaussController
from src.controllers.gaussSiedelController import GaussSiedelController

def cabecalho():
    print('Olá, seja bem-vindo a um script de execução de algoritmo de Escalonamento de Gauss')
    print('Este script foi elaborado por Daniel Soares, https://github.com/ssdaniel96')
    print('UNASP-HT, 2021, Engenharia da Computação, Métodos Numéricos Computacionais, sob orientação da Profª. Thais Michelli\n')

def escolher_metodo():
    print('1. Gauss\n2. Gauss Siedel')
    try:
        opcao = int(input('Digite a opcao: '))
    except:
        print('Valor incorreto, digite um valor numérico entre 1 e 2.')
        return escolher_metodo()
    return opcao

def chamar_metodo():
    escolha = escolher_metodo()
    if (escolha == 1):
        GaussController()
    elif (escolha == 2):
        GaussSiedelController()
    else:
        print('Valor não existe, encerrando...')
        
def main():
    cabecalho()
    chamar_metodo()

if __name__ == '__main__':
    main()

