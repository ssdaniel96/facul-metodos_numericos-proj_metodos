class Lagrange:
    x_list: list = []
    y_list: list = []
    x_point: float = 0
    y_point: float = 0
    k_degree: int

    def __init__(self, x_list: list, y_list: list, x_point: int):
        self.x_list = x_list
        self.k_degree = len(x_list)-1
        self.y_list = y_list
        self.x_point = x_point

    @staticmethod
    def calcular_Ln(x_point: float, xn: float, xk: float):
        value = (x_point-xk)/(xn-xk)
        return value

    def __calcular_Ln(self, n: int):
        ln = 1
        for k in range(self.k_degree+1):
            if (k != n):
                ln *= Lagrange.calcular_Ln(self.x_point,
                                           self.x_list[n], 
                                           self.x_list[k])
        return ln * self.y_list[n]

    def calcular_y(self):
        self.y_point = 0
        for k in range(self.k_degree+1):
            self.y_point += self.__calcular_Ln(k)
        return self.y_point