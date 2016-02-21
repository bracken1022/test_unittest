
from rome import Rome

class Symbol(object):


    def __init__(self):
        self.rome = Rome()
        self.symbolToRome = {}

    def value(self, symbolStr):
        return self.symbolToRome.get(symbolStr, "NULL")

    def AddCondition(self, conditionStr):
        
        if False == isinstance(conditionStr, basestring):
            return False

        if 2 != conditionStr.count(" "):
            return False

        if 1 != conditionStr.count(" is "):
            return False

        conditions = conditionStr.split(" ")

        symbol = conditions[0]
        romeNumber = conditions[-1]

        if False == self.rome.IsValid(romeNumber):
            return False

        self.symbolToRome.setdefault(symbol, romeNumber)
        return True

    def Calculate(self, symbolList):
        for symbol in symbolList:
            if symbol not in self.symbolToRome:
                return False, 0

        romeList = [self.symbolToRome[symbol] for symbol in symbolList]
        return self.rome.Calculate(romeList)
