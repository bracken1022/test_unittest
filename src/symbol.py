
from rome import Rome
from inputValidation import SymbolInputValidation


        

class Symbol(object):


    def __init__(self):
        self.symbolToRome = {}

    def value(self, symbolStr):
        return self.symbolToRome.get(symbolStr, "NULL")

    def AddCondition(self, conditionStr):
        symbolInputValidation = SymbolInputValidation(conditionStr)
        if symbolInputValidation.IsInValid():
            return False

        conditions = conditionStr.split(" ")

        symbol = conditions[0]
        romeNumber = conditions[-1]

        self.symbolToRome.setdefault(symbol, romeNumber)
        return True

    def CalculateResult(self, symbolList):
        for symbol in symbolList:
            if symbol not in self.symbolToRome:
                return False, 0

        romeList = [self.symbolToRome[symbol] for symbol in symbolList]
        return self.rome.Calculate(romeList)


class SymbolRomeConversion(Symbol):


    def __init__(self):
        super(SymbolRomeConversion, self).__init__()
        self.rome = Rome()

    def AddCondition(self, conditionStr):
        if False == super(SymbolRomeConversion, self).AddCondition(conditionStr):
            return False

        romeNumber = conditionStr.split(" ")[-1]
        return self.rome.AppendRome(romeNumber)
        
