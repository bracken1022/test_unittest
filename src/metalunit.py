


class MetalUnit(object):
    

    def __init__(self):
        self.metalUnit = {}

    def AddCondition(self, metalName, value):
        self.metalUnit.setdefault(metalName, value)

    def CalculateResult(self, metalName):
        return self.metalUnit.get(metalName, False)
