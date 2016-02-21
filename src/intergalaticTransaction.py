
from symbol import Symbol

class IntergalaticTransaction(object):


    def __init__(self):
        self.symbol = Symbol()
        self.metalUnit = {}

    def SetCondition(self, conditionStr):
        if not isinstance(conditionStr, basestring):
            return False

        if 0 == conditionStr.count("Credit"):
            return self.symbol.AddCondition(conditionStr)

        symbolList = conditionStr.split(" ")
        metalPosition = symbolList.index("is") - 1
        result, number = self.symbol.Calculate(symbolList[0:metalPosition])
        if result == False:
            return False
        
        metalNumber = int(symbolList[metalPosition + 2]) / float(number)
        self.metalUnit.setdefault(symbolList[metalPosition], metalNumber)
        return True

    def CalculateResult(self, inputStr):
        if 0 == inputStr.count(" "):
            result, number = self.symbol.Calculate([inputStr])
            if False == result:
                return self.metalUnit.get(inputStr, False)
            else:
                return number

        

        symbolList = inputStr.split(" ")
        metalValue = self.metalUnit.get(symbolList[-1], 1)


        if 1 == metalValue:
            result, number = self.symbol.Calculate(symbolList)
        else:
            result, number = self.symbol.Calculate(symbolList[0:-1])

        if True == result:
            return number * metalValue

        return False


    def symbolValue(self, symbolStr):
        return self.symbol.value(symbolStr)
