class ValueHelper:
    @staticmethod
    def get(type: type, text: str):
        try:
            value = type(input(text))
        except:
            print('Insira um valor válido')
            return ValueHelper.get(type, text)
        return value

def pegar_valor_entre_limites(type: type, min, max, message: str):
    try:
        opcao = int(input(message))
        if opcao > max or opcao < min:
            raise Exception()
    except:
        print(f'Valor incorreto, digite um valor numérico entre {min} e {max}.')
        return pegar_valor_entre_limites(type, min, max, message)
    return opcao

def pegar_valor(type: type, message: str):
    try:
        value = type(input(message))
    except:
        print('Insira um valor válido')
        return ValueHelper.get(type, message)
    return value

def criar_lista(type: type, n: int, separator: str, message: str):
    line = input(message)
    values = line.split(separator)
    try:
        values = [type(i) for i in values]
        if (len(values) != n):
            print(f'O total de elementos (len(values)) da lista é diferente do solicitado ({n}')
            raise Exception()
    except:
        print('Um erro ocorreu, você preencheu, corretamente? Tente novamente')
        return criar_lista(type, n, separator, message)
    return values
