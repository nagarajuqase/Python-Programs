'''
name = 'nagaraju'
print(name.count('a',0,3))
print(name.find('ga'))
print(name.isalpha())
myTup = ('Hi', 'How', 'Good', 2)
print(myTup+('Hello', 'Namaskar'))
print(myTup[1:5])
print(myTup*3)


myDict = {'Name' : 'Saurabh', 'Age' : 23}
print(myDict['Name'])
print(len(myDict))
print(myDict.keys())
print(myDict.values())

myset1={1,2,6,8}
myset2={2,4,5}
print(myset1 & myset2)
print(myset1 | myset2)
print(myset1 - myset2)

num = int(input('Enter number: '))
if num <=0:
    print("Enter valid number")
else:
    sum=0
    while num > 0:
        sum+=num
        num-=1

print(sum)

a = 10
b = 20
if a is b:
    print("a is present in b")
else:
    print("a is not present in b")

list1 ={10, 20 , 30}
if a in list1:
    print("a is present in the list1")

'''
import decimal

'''
class Student:
    def __init__(self, firstName, lastName, marks):
        self.firstName = firstName;
        self.lastName = lastName
        self.marks = marks
    def fullName(self):
        return '{}{}'.format(self.firstName, self.lastName)
stu1 = Student('Naga', 'Raju', 70)
stu2 = Student('Sri', 'Kanth', 80)

print(stu1.firstName)
print(stu2.firstName)
print(stu1.fullName())

class Inherite(Student):
    pass
stu3 = Inherite('gopi', 'c', 90)
print(stu3.firstName)

'''
from decimal import *

# $1,234.00
'''name2 = '1234';
output = list[name2]
print(output)
output.insert(0,'&')
output.insert(2,',')
output.insert(6,'.')
#output.insert(7,'00')
''.join(output)
d =Decimal(output)
print(d)'''
from decimal import *
name = '1234'
'''output =name[:0] + "$" + name[:1] + "," + name[1:]
g =decimal.Decimal(str(output))
print(g)
print(name[:0] + "$" + name[:1] + "," + name[1:])

'''
def ins(name, insert_dollar, pos, insert_comma, pos2):
    val = name[:pos] + insert_dollar + name[:pos2] + insert_comma + name[pos2:]
    return val


print(ins(name, '$', 0, ',', 1))
from array import array
test_array = array('i')
print(len(test_array))

s = '1234';
print(s)
n = int(s)
print(n)
f = float(n)
print(f)
