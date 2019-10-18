import src.Nodes.Operator as Operator

class SubtractNode(Operator.Operator):
    
    def __init__(self,stk):
        super().__init__(stk)
        self.__precedence = 1

    def precedence(self):
        return self.__precedence
        
    def evaluate(self,v1,v2):
        return v1 - v2