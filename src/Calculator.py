import src.Stack as Stack
import src.Queue as Queue
import src.Factory as Factory
import re

OPERATOR_RE = re.compile(r"(\+|-|\*|\/|\^|%|\(|\)){1}")
WHITESPACE_RE = re.compile(r"(\s+)")

def convert_eq(eq):
    eq = WHITESPACE_RE.sub("",eq)
    tokenlist = OPERATOR_RE.split(eq)
    tokenlist = [x for x in tokenlist if x != ""]
    tokens = Queue.Queue()
    for token in tokenlist:
        tokens.enqueue(token)
    return tokens
class Calculator:

    def __init__(self):
        self.__postfix = Queue.Queue()
        self.__calculator_stack = Stack.Stack()
        self.__factory = Factory.Factory(self.__calculator_stack)

    def calculate(self):
        while not self.__postfix.is_empty():    # while the postfix queue is not empty,
            self.__postfix.dequeue().execute()  # dequeue and execute it.
        return self.__calculator_stack.peek()   # the top of the stack will now be the answer.

    def __infix_to_postfix(self,tokens):
        expression = Stack.Stack()
        node = None
        
        while not tokens.is_empty(): # while there are tokens to handle...
            token = tokens.dequeue() # get the token on top and handle it

            if token == "+":
                node = self.__factory.create_addition()
            elif token == "-":
                node = self.__factory.create_subtraction()
            elif token == "*":
                node = self.__factory.create_multiplication()
            elif token == "/":
                node = self.__factory.create_division()
            elif token == "%":
                node = self.__factory.create_modulo()
            elif token == "^":
                node = self.__factory.create_exponent()
            elif token == "(":
                self.__infix_to_postfix(tokens) # we can treat everything in paranthesis
                continue                        # as it's own expression.
            elif token == ")":
                while not expression.is_empty():              # we pop from our sub-expression
                    self.__postfix.enqueue(expression.pop())  # and add it to our postfix queue
                return
            else: # values
                i = float(token)
                node = self.__factory.create_value(i)
                self.__postfix.enqueue(node)
                continue
            
            while (not expression.is_empty() and (expression.peek().precedence() >= node.precedence())):
                self.__postfix.enqueue(expression.pop()) # order of operations
            expression.push(node)

        while not expression.is_empty():
            self.__postfix.enqueue(expression.pop())


    def infix_to_postfix(self,infix):      # this function just turns a string into a
        tokens = convert_eq(infix)         # a queue of tokens that our real infix to
                                           # postfix function can handle.

        self.__infix_to_postfix(tokens)
