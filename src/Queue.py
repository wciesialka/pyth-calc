class Queue:

    def __init__(self):
        self.__a = []
        self.__length = 0

    def enqueue(self,val):
        self.__a.insert(0,val)
        self.__length += 1

    def dequeue(self):
        if self.__length == 0:
            raise RuntimeError("Cannot dequeue from empty queue!")
        else:
            self.__length -= 1
            return self.__a.pop()

    def peek(self):
        return self.__a[-1]

    def empty(self):
        self.__a = []
        self.__length = 0

    def length(self):
        return self.__length

    def is_empty(self):
        return self.__length == 0

    def __len__(self):
        return self.length()
    