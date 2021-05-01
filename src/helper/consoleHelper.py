import os

def limpar_console():
    clsc = ('cls' if os.name == 'nt' else 'clear')
    os.system(clsc)
