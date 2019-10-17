import Stack
import Queue

class Calculator:

    def __init__(self):
        self.__postfix = Queue.Queue()
        self.__calculator_stack = Stack.Stack()
        self.__factory = None

    def calculate(self):
        while not self.__postfix.is_empty():
            self.__postfix.dequeue().execute()
        return self.__calculator_stack.peek()

    def __infix_to_postfix(self,tokens):
        expression = Stack.Stack()
        node = None
        
        while not tokens.is_empty():
            token = tokens.dequeue()

            if token == "+":
                self.__factory.create_addition()
            elif token == "-":
                self.__factory.create_subtraction()
            elif token == "*":
                self.__factory.create_multiplication()
            elif token == "/":
                self.__factory.create_division()
            elif token == "%":
                self.__factory.create_modulo()
            elif token == "(":
                self.__infix_to_postfix(tokens)
            elif token == ")":
                while not expression.is_empty():
                    self.__postfix.enqueue(expression.pop())
                return
            else:
                i = float(token)
                node = self.__factory.create_value(i)
                self.__postfix.enqueue(node)
            
            while (not expression.is_empty() and (expression.peek().precedence() >= node.precedence())):
                self.__postfix.enqueue(expression.pop())
            expression.push(node)

        while not expression.is_empty():
            self.__postfix.enqueue(expression.pop())


    def infix_to_postfix(self,infix):
        initial_tokens = infix.split(" ")
        tokens = Queue.Queue()

        for token in initial_tokens:
            tokens.enqueue(token)

        self.__infix_to_postfix(tokens)
