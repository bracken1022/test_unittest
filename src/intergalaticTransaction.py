
from symbol import Symbol

class IntergalaticTransaction(object):


    def __init__(self):
        self.symbol = Symbol()

    def SetCondition(self, conditionStr):
        if not isinstance(conditionStr, basestring):
            return False

        if 0 == conditionStr.count("Credit"):
            return self.symbol.AddCondition(conditionStr)

        symbolList = conditionStr.split(" ")
        metalPosition = symbolList.index("is") - 1
        number = self.symbol.Calculate(symbolList[0:metalPosition])

        

    def symbolValue(self, symbolStr):
        return self.symbol.value(symbolStr)
