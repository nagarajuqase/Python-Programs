'''num = [5,1,9,1,5,2,3,2,8,2]
num[4:]
[5, 2, 3, 2, 8, 2]
num[:4]
[5, 1, 9, 1]
num[-4:]
[3, 2, 8, 2]
num[:-4]
[5, 1, 9, 1, 5, 2]
num[::-1]
[2, 8, 2, 3, 2, 5, 1, 9, 1, 5]
num[-1::]
[2]'''
num = [5,1,9,1,5,2,3,2,8,2]
print(num.count(2))
print num[4:]
print(num[::-1])
print(num)
num.reverse()
print(num)
s = list(set(num))
print(s)
# print(''.join(str(s)))
unique = []
duplicate = []
for i in num:
    if num.count(i) is 1:
        unique.append(i)
    elif num.count(i) >=2:
        if i not in duplicate:
            duplicate.append(i)

print(unique)
print(duplicate)

val = [5,1,9,1,5,2,3,2,8,2]
val2 = list(set(val))
print(val2)
print(val2[::-1])


def checkio(data):
    elements = []
    duplicates = []
    for i in data:
        if i not in elements:
            elements.append(i)
        else:
            if i not in duplicates:
                duplicates.append(i)
    return duplicates

d = [1, 3, 1, 2, 3, 5, 8, 1, 5, 2]

print (checkio(d))

s = 'IndIa'
print(s.lower())


def main():
    Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
    for i, m in enumerate(Months):
        print i, m


if __name__ == "__main__":
    main()


def main():
    for x in range(10, 20):
        if (x % 5 == 0): continue
        print x


if __name__ == "__main__":
    main()


def main():
    for x in range(10, 20):
        if (x == 15): break
        print x


if __name__ == "__main__":
    main()


def main():
    x = 0

    for x in range(2, 7):
        print x


if __name__ == "__main__":
    main()


def main():
    x = 0
    while (x < 4):
        print x
        x = x + 1


if __name__ == "__main__":
    main()

import collections
s = raw_input()
countChar = collections.Counter(s)
print(countChar)

freq = {}   # frequency of words in text
line = raw_input()
for word in line:
    freq[word] = freq.get(word,0)+1
print freq
