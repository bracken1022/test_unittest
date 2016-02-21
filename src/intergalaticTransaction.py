
from symbol import SymbolRomeConversion
from metalunit import MetalUnit
from inputValidation import IntergalaticTransactionInputValidation


class IntergalaticTransaction(object):


    def __init__(self):
        self.symbol = SymbolRomeConversion()
        self.metalUnit = MetalUnit()

    def SetCondition(self, conditionStr):
        inputValidation = IntergalaticTransactionInputValidation(conditionStr)
        if inputValidation.IsInValid():
            return False

        symResult = self.__addSymbolCondition(conditionStr)
        metalResult = self.__addMetalCondition(conditionStr)

        return (symResult or metalResult)

    #condition: glob is I
    def __addSymbolCondition(self, conditionStr):
        if 1 == conditionStr.count(" is "):
            return self.symbol.AddCondition(conditionStr)

        return False

    #condition: glob glob Silver is 35 Credits.
    def __addMetalCondition(self, conditionStr):
        if 0 == conditionStr.count("Credits"):
            return False

        wordsList = conditionStr.split(" ")
        metalPosition = wordsList.index("is") - 1

        #such as: glob glob
        symbols = wordsList[0:metalPosition]
        result, number = self.symbol.CalculateResult(symbols)
        if not result: return False

        #such as: 35 Credits
        totalValue = wordsList[metalPosition + 2]
        metalValue = int(totalValue) / float(number)

        metalName = wordsList[metalPosition]
        self.metalUnit.AddCondition(metalName, metalValue)
        return True

    def CalculateResult(self, inputStr):

        #input: prob
        if 0 == inputStr.count(" "):
            result, value = self.symbol.CalculateResult([inputStr])
            if result == False:
                return self.metalUnit.CalculateResult(inputStr)
            else:
                return value

        
        #input: prob prob Gold
        symbolList = inputStr.split(" ")
        metalValue = self.metalUnit.CalculateResult(symbolList[-1])
        if False == metalValue:
            metalValue = 1


        if 1 == metalValue:
            result, number = self.symbol.CalculateResult(symbolList)
        else:
            result, number = self.symbol.CalculateResult(symbolList[0:-1])

        if True == result:
            return number * metalValue

        return False

        

    def symbolValue(self, symbolStr):
        return self.symbol.value(symbolStr)
