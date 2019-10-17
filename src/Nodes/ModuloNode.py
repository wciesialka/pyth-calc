import src.Nodes.Operator as Operator

class ModuloNode(Operator.Operator):
    
    def __init__(self,stk):
        super().__init__(stk)
        
    def evaluate(self,v1,v2):
        if v2 == 0:
            raise RuntimeError("Cannot modulo by zero!")
        else:
            return v1 % v2