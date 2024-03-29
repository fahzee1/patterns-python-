"""Implementation of the iterator pattern with a generator"""

def count_to(count):
    """Counts by word numbers, up to a maximum of five"""
    numbers = ["one", "two", "three", "four", "five"]
    # enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over sequence
    for pos, number in zip(numbers, range(count)):
        yield number

# Test the generator
count_to_two = lambda : count_to(2)
count_to_five = lambda : count_to(5)

print('Counting to two...')
for number in count_to_two():
    print(number, end=' ')

print()

print('Counting to five...')
for number in count_to_five():
    print(number, end=' ')

print()
