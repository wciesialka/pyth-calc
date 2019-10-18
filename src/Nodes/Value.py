class Value():
    
    def __init__(self,stk,rv):
        self.__s = stk
        self.__value = rv

    def execute(self):
        self.__s.push(self.__value)

    def precedence(self):
        return -1

    def __str__(self):
        return str(self.__value)