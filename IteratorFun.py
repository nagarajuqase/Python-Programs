# iteration is the process of taking one element at a time in a row of elements
# iterable is an object that is, well, iterable, which simply put, means that it can be used in iteration
# iterator is an object that defines how to actually do the iteration--specifically what is the next element.

for element in [1, 2, 3]:
    print element
for element in (1, 2, 3):
    print element
for key in {'one':1, 'two':2}:
    print key
for char in "123":
    print char
for line in open("TextRead2.txt"):
    print line,

s = 'abc'
it = iter(s)
print it.next()
print it.next()
print it.next()

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index-1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)
for char in rev:
   print char

rev = Reverse('spam')
reversed('spam')
for char in rev:
   print char

class zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)

class zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


class bidirectional_iterator(object):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def next(self):
        try:
            result = self.collection[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration
        return result

    def prev(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.collection[self.index]

    def __iter__(self):
        return self

nextIter = bidirectional_iterator('Good')
iter(nextIter)
for each in nextIter:
    print each