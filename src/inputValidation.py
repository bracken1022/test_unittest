

class InputValidation(object):


    def __init__(self, input):
        self.input = input
        pass


    def IsInValid(self):
        if not isinstance(self.input, basestring):
            return True

        return False


class IntergalaticTransactionInputValidation(InputValidation):


    def IsValid(self):
        pass


class SymbolInputValidation(InputValidation):



    def IsInValid(self):
        if super(SymbolInputValidation, self).IsInValid():
            return True

        if 2 != self.input.count(" "):
            return True

        if 1 != self.input.count(" is "):
            return True

        return False


    def IsValid(self):
        pass


