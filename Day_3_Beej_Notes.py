"""
What Hash Tables Solve

- We need to look up some data quickly
    - Some data that was slow to generate or obtain

In lieu of linear search...

It doesn't matter if _n_ is small. O(n) vs O(1)

Any time-consuming process:
- Memoization (caching the results of a function call) (caching is a more general term used)
- Network caching
- Indexing
- Removing duplicates from lists
- Detecting duplicates
- Counting duplicates


"""
#Fibonacci. Every number is the sum of the previous 2 numbers.
#    fib(0): 0
#     fib(1): 1
#     fib(n): fib(n-1) + fib(n-2)

# def fib(n):
#     if n <= 1: return n

#     return fib(n-1) + fib(n-2)

# for i in range(100):
#     print(f'{i:3} {fib(i)}')
#This option ABOVE ^^^ goes really slow once it gets to 35th fibonacci number, it will never be finished in this lifetime! It will have to produce 2^34 levels of 2nd and 3rd numbers, finding the number value each time, which will be over 17 billion levels.

#This option BELOW stores the numbers in a cache, so the computer does not have to generate the number each time, its already stored.
# cache = {}

# def fib(n):
#     if n <= 1: return n

#     if n not in cache:
#         cache[n] = fib(n-1) + fib(n-2)
#     return cache[n]

# for i in range(100):
    #print(f'{i:3} {fib(i)}')

######################

d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

items = list(d.items())

items.sort()

for i in items:
    print(f'{i[0]}: {i[1]}')
    #This will print key: value in a sorted order alphabetically by first letter

