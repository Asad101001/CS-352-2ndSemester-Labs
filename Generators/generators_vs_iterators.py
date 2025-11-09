import sys

# Same Functionality, Different Approach


# Iterator Version
class CountIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        self.current += 1
        return self.current


# Generator Version
def count_generator(n):
    for i in range(1, n + 1):
        yield i


print("Iterator:", list(CountIterator(5)))
print("Generator:", list(count_generator(5)))

# Memory Usage Comparison
n = 1000000
list_data = [x for x in range(n)]
gen_data = (x for x in range(n))

print(f"List: {sys.getsizeof(list_data):,} bytes")
print(f"Generator: {sys.getsizeof(gen_data):,} bytes")


# Reusability Test
class Reusable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)


def one_time(data):
    for item in data:
        yield item


reusable = Reusable([1, 2, 3])
print("Iterator 1st:", list(reusable))
print("Iterator 2nd:", list(reusable))

gen = one_time([1, 2, 3])
print("Generator 1st:", list(gen))
print("Generator 2nd:", list(gen))  # Empty!


# Pipeline Example (Generators Excel)
def read_data():
    for i in range(10):
        yield i


def square(nums):
    for n in nums:
        yield n**2


def even(nums):
    for n in nums:
        if n % 2 == 0:
            yield n


result = even(square(read_data()))
print("Pipeline:", list(result))
