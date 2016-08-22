from copy import deepcopy as copy
import random

class RandomNumberIterator(object):
    def __init__(self, generated_numbers=None):
        self._generated_numbers = copy(generated_numbers or [])
        self.count = 0
        
    def __iter__(self):
        return RandomNumberIterator(self._generated_numbers)
        #self.count = 0
        #return self

    def next(self):
        if self.count == 3:
            raise StopIteration()
        
        n = random.randint(0, 10)
        while n in self._generated_numbers:
            n = random.randint(0, 10)

        self._generated_numbers.append(n)
        self.count += 1
        return n

    __next__ = next

random_numbers = RandomNumberIterator()

for number in random_numbers:
    print(number)

print("2nd time")
for number in random_numbers:
    print(number)