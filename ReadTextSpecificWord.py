f = open('D:\\RobotFramework_Selenium\\TextRead.txt', 'r')
'''contents = f.readline()
count = contents.count("is")
print count'''

countword = 0
for line in f:
   # print line
    if 'is' in line:
        countword +=1
print countword

s = 'i love india i love india'
countlove=0
for line in s.split(' '):
    if 'love' in line:
        countlove+=1
print countlove