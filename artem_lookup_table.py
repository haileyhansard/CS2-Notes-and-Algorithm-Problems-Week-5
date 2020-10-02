import math
import time

"""
#The Lookup Table: find ways to pre-build data.
"""

#Inverse square root is 1 / square root of number
# Relatively time consuming

def get_inverse_square(num):
    return 1 / math.sqrt(num)

# We need to constantly get the inverse square roots of numbers between 1 and 1000

print(get_inverse_square(500))


#What should our lookup table look like?
# Keys will be numbers
# Values will be results of get_inverse_square

def build_lookup_table():
    lookup_table = {}
    for i in range(1, 1001):
        lookup_table[i] = get_inverse_square(i)
    return lookup_table

sqrt_lookup_table = build_lookup_table()


print(sqrt_lookup_table[3])
print(sqrt_lookup_table[982])
print(sqrt_lookup_table[234])


#Can use this to test the speed of each
t1 = time.time()
get_inverse_square(556)
print("Time to find inverse root: %f " % (time.time() - t1))

t1 = time.time()
print(sqrt_lookup_table[556])
print("Time to lookup inverse root: %f " % (time.time() - t1))