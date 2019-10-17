import src.Nodes.Operator as Operator

class SubtractNode(Operator.Operator):
    
    def __init__(self,stk):
        super().__init__(stk)
        
    def evaluate(self,v1,v2):
        return v1 - v2