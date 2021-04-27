class ValueHelper:
    @staticmethod
    def get(type: type, text: str):
        try:
            value = type(input(text))
        except:
            print('Insira um valor válido')
            return ValueHelper.get(type, text)
        return value