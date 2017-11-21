# Generators are a simple and powerful tool for creating iterators.
# They are written like regular functions but use the yield statement whenever they want to return data

def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print char


def reverse(data):
    for index in range(0, len(data), 1):
        yield data[index]


for char in reverse('Sample'):
    print char

sum_val=sum(i*i for i in range(10))                 # sum of squares
print sum_val

sum_val=[i*i for i in range(10)]                 # square value
print sum_val

sum_val=[i*i*i for i in range(10)]                 # cube value
print sum_val

def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i

def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(seq.next())
    except StopIteration:
        pass
    return result

print take(5, squares())


def putNumbers(n):
    i = 0
    while i < n:
        i = i + 1
        if i % 7 == 0:
            yield i


for i in putNumbers(100):
    print i

def yrange(n):
    i = 0
    while i < n:
        i += 1
        yield i

for i in yrange(3):
    print i