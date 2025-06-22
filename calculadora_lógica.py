class Calculadora:
    def __init__(self): 
        self.expressao = ""
    #armazena oq o usuário digitou até o momento

    def inserir(self, valor):
        self.expressao += valor
    # inserir os valores, ele conatena, apenas

    def apagar_ultimo(self):
        self.expressao = self.expressao[:-1]
    # apaga o último valor

    def limpar(self):
        self.expressao = ""
    # limpa tudo

    def calcular(self):
        expressao_py = self.expressao.replace('×', '*').replace('÷', '/') #converte os operandos para que o python entenda
        try:
            resultado = eval(expressao_py)
            self.expressao = str(resultado)
            return self.expressao
        except Exception:
            self.limpar()
            return "Erro"

    def calcular_porcentagem(self):
        try:
            expressao_py = self.expressao.replace('×', '*').replace('÷', '/')
            valor = eval(expressao_py)
            resultado = valor / 100
            self.expressao = str(resultado)
            return self.expressao
        except Exception:
            self.limpar()
            return "Erro"
