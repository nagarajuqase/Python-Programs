'''num = int(input("Enter number: "))
fact =1;
if(num<0):
    print("must be positive")
elif(num==0):
    print("factorial nunber is 1")
else:
    for i in range(1,num+1):
        print(i)
        fact = fact*i
print(fact)
print(i)
'''
def factorialnum(number=int(input("Enter number: "))):
    if (number < 0):
        return 0
    elif (number == 0):
       return 1
    else:
        return(number*factorialnum(number-1))
print(factorialnum())