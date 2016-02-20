ROME_TO_DEC = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

class Rome(object):
    

    def IsValid(self, romeStr):
        if romeStr not in ROME_TO_DEC:
            return False
        
        return True

    def Calculate(self, romeList):
        return 1
        pass
