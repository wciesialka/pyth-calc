import src.Nodes.Operator as Operator

class ExponentNode(Operator.Operator):
    
    def __init__(self,stk):
        super().__init__(stk)
        self.__precedence = 3

    def precedence(self):
        return self.__precedence
        
    def evaluate(self,v1,v2):
        return v1 ** v2