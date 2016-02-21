
from rome import Rome
from inputValidation import SymbolInputValidation


class Symbol(object):


    def __init__(self):
        self.rome = Rome()
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

        if False == self.rome.IsValid(romeNumber):
            return False

        self.symbolToRome.setdefault(symbol, romeNumber)
        return True

    def CalculateResult(self, symbolList):
        for symbol in symbolList:
            if symbol not in self.symbolToRome:
                return False, 0

        romeList = [self.symbolToRome[symbol] for symbol in symbolList]
        return self.rome.Calculate(romeList)
