ROME_TO_DEC = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

class Rome(object):
    

    def __init__(self):
        self.romeNumber = []

    def IsValid(self, romeStr):
        if romeStr not in ROME_TO_DEC:
            return False
        
        return True

    def AppendRome(self, romeNumber):
        
        if not self.IsValid(romeNumber):
            return False

        self.romeNumber.append(romeNumber)
        return True

    def Calculate(self, romeList):
        if not self.__matchRepeatedRules(romeList):
            return (False, 0)

        numberList = [ROME_TO_DEC[rome] for rome in romeList]

        for i in range(0, len(romeList) - 1):
            if self.__matchSubstractedRules(romeList[i], romeList[i + 1]):
                numberList[i] = -ROME_TO_DEC[romeList[i]]

        return True, sum(numberList)

    def __matchSubstractedRules(self, romeNumeral, nextRomeNumeral):
        
        if (self.__substractRules_I(romeNumeral, nextRomeNumeral) or 
        self.__substractRules_X(romeNumeral, nextRomeNumeral) or
        self.__substractRules_C(romeNumeral, nextRomeNumeral)):
            return True
        
        return False


    def __substractRules_I(self, symbol, nextSymbol):
        if symbol == 'I' and (nextSymbol == 'V' or  nextSymbol == 'X'):
            return True
        
        return False

    def __substractRules_X(self, symbol, nextSymbol):
        if symbol == 'X' and (nextSymbol == 'L' or nextSymbol == 'C'):
            return True

        return False

    def __substractRules_C(self, symbol, nextSymbol):
        if symbol == 'C' and (nextSymbol == 'D' or nextSymbol == 'M'):
            return True

        return False

    def __matchRepeatedRules(self, romeList):
        romeSuccession = []
        lastPos = 0
        firstPos = 0
        for i in range(1, len(romeList)):
            if romeList[i] == romeList[i-1]:
                lastPos = i
            else:
                romeSuccession.append(romeList[firstPos:lastPos + 1])
                firstPos = lastPos + 1
                lastPos = i

        romeSuccession.append(romeList[firstPos:lastPos + 1])

        for succession in romeSuccession:
            if len(succession) == 3:
                element = succession[0]
                if element not in ["I", "X", "C", "M"]:
                    return False

            if len(succession) > 3:
                return False
            
        return True
