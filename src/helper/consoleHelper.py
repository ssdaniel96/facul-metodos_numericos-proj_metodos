import os
class ConsoleHelper:
    @staticmethod
    def limpar_console():
        clsc = ('cls' if os.name=='nt' else 'clear')
        os.system(clsc)