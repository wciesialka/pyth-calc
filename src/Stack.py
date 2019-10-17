class Stack:

    def __init__(self):
        self.__length = 0
        self.__a = []

    def push(self,val):
        self.__length += 1
        self.__a.insert(self.__length,val)
    
    def pop(self):
        if self.__length == 0:
            raise RuntimeError("Cannot pop from empty stack!")
        else:
            self.__length -= 1
            return self.__a.pop()

    def peek(self):
        return self.__a[-1]

    def length(self):
        return self.__length

    def empty(self):
        self.__a = []
        self.__length = 0

    def is_empty(self):
        return self.__length == 0

    def __len__(self):
        return self.length()