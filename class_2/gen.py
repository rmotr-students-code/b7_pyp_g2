import random


def random_number_generator(n=3):
    i = 0
    while i < n:
        yield random.randint(0, 100)
        i += 1

    # yield random.randint(0, 100)


gen = random_number_generator(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))