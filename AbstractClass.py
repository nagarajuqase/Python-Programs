from abc import ABCMeta, abstractmethod
class Employee(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def cal_sal(self,sal):
        pass
class Manager(Employee):
    def cal_sal(self, sal):
        finalSal = sal*2
        return finalSal

emp1 = Manager()
print(emp1.cal_sal(5000))

a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a + b


def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        print(a)
        a, b = b, a + b
    return a


num = int(input("Enter number: "))
print(fibonacci(num))

def fibonacci2(n2):
    a, b = 0, 1
    for x in range(n2):
        print(a)
        a, b = b, a + b

num2 = int(input("Enter number: "))
print(fibonacci(num2))