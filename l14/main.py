import random


class Int(int):
    def __add__(self, __value: int) -> int:
        if ((self == 2) and (__value == 2)):
            return 5
        return super().__add__(__value)
    

class List(list):
    def append(self, __object: int) -> None:
        if (len(self) < 10):
            return super().append(__object)
        else:
            raise "List is full"


class List2(list):
    def append(self, __object: int) -> None:
        if (self.count(__object) == 0):
            return super().append(__object)
        else:
            return None

    
if __name__ == '__main__':
    a = Int(2)
    print(a + 2)
    
    l = List()
    for x in range(9):
        l.append(x)
    print(l)
    print(len(l))
    
    l2 = List2()
    for x in range(50):
        l2.append(random.randrange(0,10))
    print(l2)
    print(len(l2))
