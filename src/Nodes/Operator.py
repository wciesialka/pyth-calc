class Operator():

    def __init__(self,stk):
        self.__s = stk

    def precedence(self):
        return self.__precedence

    def evaluate(self,v1,v2):
        pass

    def execute(self):
        v2 = self.__s.pop()
        v1 = self.__s.pop()
        result = self.evaluate(v1,v2)

        self.__s.push(result)