class FinanceiroPessoal:
    def __init__(self,conta,conta1,conta2):
        self.salario_bruto = float(2154.19)
        self.cartao = float(conta)
        self.cartao1 = float(conta1)
        self.cartao2 = float(conta2)
        self.internet = float(75.00)
        self.spotify = float(12.5)
        self.celular_pai = float(90.5)
        self.faculdade = float(367.51)
    
    @property
    def salario(self):
        salario_liquido = self.salario_bruto - ((self.salario_bruto * 9)/100)
        salario_liquido = round(salario_liquido,2)
        return salario_liquido
    
    def conta_mae(self):
        conta1 = (self.cartao + self.internet + self.spotify + self.celular_pai)
        return conta1
    
    @property
    def atual_cartao1(self):
        return self.cartao1
    
    @property
    def atual_cartao2(self):
        return self.cartao2
    
    @property
    def exibe_faculdade(self):
        return self.faculdade
    
    
    
victtor = FinanceiroPessoal(34.80,39.90,96)





