'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''

l = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))

print ','.join(l)

'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''
print 'Enter factorial number'


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


x = int(raw_input())
print fact(x)

'''With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()'''

print 'Enter integer square number'
n = int(raw_input())
d = dict()
for i in range(1, n + 1):
    d[i] = i * i

print d

'''Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple'''

print 'Enter list of values'
values = raw_input()
l = values.split(",")
t = tuple(l)
print l
print t

'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters'''
print 'Enter the String'


class InputOutString(object):
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = raw_input()

    def print_string(self):
        print self.s.upper()


strObj = InputOutString()
strObj.get_string()
strObj.print_string()

'''Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. '''

print 'Enter list of values'
import math

c = 50
h = 30
value = []
items = [x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))

print ','.join(value)

'''Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.'''

print 'Enter list of words'
input_str = raw_input()
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col

print multilist

'''Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world'''

print 'Enter list of words'
items = [x.strip(' ') for x in raw_input().split(',')]
items.sort()
print ','.join(items)

'''Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT'''

lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print sentence

'''Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.'''

print 'Enter the words of statement'
s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))

'''Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.'''

value = []
items = [x for x in raw_input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp % 5:
        value.append(p)

print ','.join(value)

'''Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.'''

values = []
for i in range(1000, 3001):
    s = str(i)
    if int(s) % 2 == 0:
        # if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print ",".join(values)

'''Write a program that accepts a sentence and calculate the number of letters, digits, upper case letters and lower case letters.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

s = raw_input()
d = {"DIGITS": 0, "LETTERS": 0, "UPPERCASE": 0, "LOWERCASE": 0, "SPACES": 0}
for c in s:
    if c.isdigit():
        d["DIGITS"] += 1
    elif c.isalpha():
        d["LETTERS"] += 1
        if c.islower():
            d["LOWERCASE"] += 1
        else:
            d["UPPERCASE"] += 1
    elif c.isspace():
        d["SPACES"] += 1
    else:
        pass

print "DIGITS", d["DIGITS"]
print "LETTERS", d["LETTERS"]
print "LOWERCASE", d["LOWERCASE"]
print "UPPERCASE", d["UPPERCASE"]
print "SPACES", d["SPACES"]

'''Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106'''

a = raw_input()
n1 = int("%s" % a)
print n1
n2 = int("%s%s" % (a, a))
print n2
n3 = int("%s%s%s" % (a, a, a))
print n3
n4 = int("%s%s%s%s" % (a, a, a, a))
print n4
print n1 + n2 + n3 + n4

'''Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9'''

values = raw_input()
numbers = [x for x in values.split(",") if int(x) % 2 != 0]
print ",".join(numbers)

'''Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500'''

class Customer(object):

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        print(self.balance)
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        print(self.balance)
        return self.balance

if __name__ == '__main__':
    c = Customer('Custermer1',300)
    c.deposit(300)
    c.withdraw(200)
    c.deposit(100)

'''A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1'''
import re
p = raw_input('Input your password\n')
x = True
while x:
    if len(p) < 6 or len(p) > 12:
        break
    elif not re.search("[a-z]", p):
        break
    elif not re.search("[0-9]", p):
        break
    elif not re.search("[A-Z]", p):
        break
    elif not re.search("[$#@]", p):
        break
    elif re.search("\s", p):
        break
    else:
        print("Valid Password")
        x = False
        break

if x:
    print("Not a Valid Password")

'''You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]'''

from operator import itemgetter

l = []
while True:
    s = raw_input()
    if not s:
        break
    l.append(tuple(s.split(",")))

l = sorted(l, key=itemgetter(0, 1, 2))
print l
for ls in l:
    print ','.join(ls)

'''Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield'''

def putNumbers(n):
    i = 0
    while i < n:
        i = i + 1
        if i % 7 == 0:
            yield i


for i in putNumbers(100):
    print i

'''A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2'''

import math
pos = [0,0]
while True:
    s = raw_input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print int(round(math.sqrt(pos[1]**2+pos[0]**2)))

'''Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1'''

freq = {}   # frequency of words in text
line = raw_input()
for word in line.split(' '):
    freq[word] = freq.get(word,0)+1
print freq

'''Write a method which can calculate square value of number

Hints:
    Using the ** operator'''

def square(num):
    return num ** 2

print square(2)
print square(3)

''' Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later'''


class Person:
    # Define the class parameter "name"
    name = "Person"

    def __init__(self, name=None):
        # self.name is the instance parameter
        self.name = name


jeffrey = Person("Jeffrey")
print "%s name is %s" % (Person.name, jeffrey.name)

nico = Person()
nico.name = "Nico"
print "%s name is %s" % (Person.name, nico.name)

'''Define a function which can compute the sum of two numbers.

Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.
'''

def SumFunction(number1, number2):
	return number1+number2

print SumFunction(1,2)

'''Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.'''

def printValue(s1,s2):
	print int(s1)+int(s2)

printValue("3","4") #7

'''Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:

Use + to concatenate the strings'''

def printValue(s1,s2):
	print s1+s2

printValue("3","4") #34

'''Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
'''


def printValue(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print s1
    elif len2 > len1:
        print s2
    else:
        print s1
        print s2


printValue("one", "three")

'''Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.'''

def checkValue(n):
    if n % 2 == 0:
        print "It is an even number"
    else:
        print "It is an odd number"

n1 = int(raw_input())
checkValue(n1)

'''Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.'''

def printDict():
    d = dict()
    d[1] = 1
    d[2] = 2 ** 2
    d[3] = 3 ** 2
    print d
printDict()

'''Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.'''


def printDict():
    d = {}
    for i in range(1, 21):
        d[i] = i ** 2
    print d


printDict()

'''Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.'''

def printDict():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    for (k, v) in d.items():
        print v

printDict()

'''Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.'''

def printList():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print li

printList()

'''Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list'''

def printList():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print li[:5]


printList()

'''Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

Hints:

Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.'''

tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
li = list()
for i in tp:
    if i % 2 == 0:
        li.append(i)

tp2 = tuple(li)
print tp2

'''Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". '''

s= raw_input()
if s=="yes" or s=="YES" or s=="Yes":
    print "Yes"
else:
    print "No"

'''Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.'''

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print evenNumbers

'''Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.'''

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print evenNumbers

'''Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:

Use filter() to filter elements of a list.
Use lambda to define anonymous functions.'''

evenNumbers = filter(lambda x: x%2==0, range(1,21))
print evenNumbers

'''Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.'''

class American(object):
    @staticmethod
    def printNationality():
        print "America"

anAmerican = American()
anAmerican.printNationality()
American.printNationality()

'''Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass.'''

class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print anAmerican
print aNewYorker

'''Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.'''

class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print aRectangle.area()

'''Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.'''

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print aSquare.area()






