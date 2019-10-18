import src.Nodes.Value as Value
import src.Nodes.AddNode as AddNode
import src.Nodes.DivideNode as DivideNode
import src.Nodes.ModuloNode as ModuloNode
import src.Nodes.MultiplyNode as MultiplyNode
import src.Nodes.SubtractNode as SubtractNode
import src.Stack as Stack

class Factory:

    def __init__(self, stk):
        self.__s = stk

    def create_value(self,val):
        return Value.Value(self.__s,val)

    def create_addition(self):
        return AddNode.AddNode(self.__s)

    def create_subtraction(self):
        return SubtractNode.SubtractNode(self.__s)

    def create_multiplication(self):
        return MultiplyNode.MultiplyNode(self.__s)

    def create_division(self):
        return DivideNode.DivideNode(self.__s)

    def create_modulo(self):
        return ModuloNode.ModuloNode(self.__s)