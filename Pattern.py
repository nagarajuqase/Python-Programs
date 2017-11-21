'''
count = 1
for i in range(6):
    # print (str(i) * i)
    print (str(i) * i)

    for j in range(0, i):
        count = count + 1


print ("Pattern C")
for e in range (11,0,-1):
    print((11-e) * ' ' + e * '*')

print ('')
print ("Pattern D")
for g in range (11,0,-1):
    print(g * ' ' + (11-g) * '*')

print ('')
print ("Pattern E")
for h in range (0,5,1):
    print(h * ' ' + (5-h) * '*')

print ('')
print ("Pattern F")
for m in range (0,5,1):
    print((5-m) * ' ' + m * '*')
'''
n = 5

# for A
print('\n'.join(['*'*i for i in range(1,n+1)]))
print('')
# for B
print('\n'.join(['*'*i for i in range(n+1,0,-1)]))
print('')

# for C
print('\n'.join([' '*(n-i) + '*'*i for i in range(n,0,-1)]))
print('')
# for D
print('\n'.join([' '*(n-i) + '*'*i for i in range(1,n+1)]))
print('')
# for E
print('\n'.join([str(i)*i for i in range(1,n+1)]))
# for E
print('\n'.join([str(i)*i for i in range(n-1,0,-1)]))
print('')
n=int(input("Enter number"));
print('\n'.join(''.join(map(str,range(1,i+1))).ljust(n,' ')for i in range(1,n+1)))
# print('\n'.join(''.join(map(str,range(i+1,1,-1))).ljust(n,' ')for i in range(n+1,1)))

