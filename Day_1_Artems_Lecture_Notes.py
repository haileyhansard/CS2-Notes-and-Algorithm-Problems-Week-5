'''
HASH TABLES
- First two days: build your own hash table from scratch
- Second two days: applications of hash tables

DAY 1 NOTES:

HASH FUNCTIONS:
 - Any string input ---> returns/outputs a Specific Number (within some range)
 - This function is deterministic, meaning, the same input will always return the same output
 - Usually return a number that is 32 or 64 bits. You can only store so much in a 32 bit number.
  - if we want to do a maximum 32 bit number, we use &= which is a bitwise operator
  - for 32 bit max, add this line: total &= 0xffffffff
  - for 64 bit max, add this line: total &= 0xffffffffffffffff

TO CONVERT STRINGS TO NUMBERS:
- We have a few ways.
1. ASCII Codes. There are codes of numbers for each letter and character. A way to map letters to numbers, which the computer understands.
2. UTF-8. Convert each character into UTF-8 numbers. 
'''

#-------> THIS IS A SIMPLE HASH FUNCTION BELOW ------>

def hashfunc(s, limit): 
#take every character in string, and convert to a number
    string_utf = s.encode()
    # print(string_utf)

    total = 0
    for c in string_utf:
        # print(c)
        total += c
        total &= 0xffffffff #limit total to 32 bits by literally manipulating the bits to this number
    return total % limit #limit is the size of the array


# print(hashfunc('hello')) #returns 532
# print(hashfunc('Hello')) #returns 500
# print(hashfunc('hello!')) #returns 565

#-------> THIS CREATES THE HASH TABLE BELOW!  

hash_table = [None] * 8 #this creates an array with 8 None values. 8 slots.

# Now, ADD items to hash_table using the hashfunc function 
#We add limit to pass into the function above
index = hashfunc('Hello', len(hash_table))
print(index)
hash_table[index] = 'Value for Hello' #it is added to index 4 because the number value of encoded "Hello" string is 500, modulo 8, is 4. 8 because that is the number of slots, the length. 0-7.
#this is looking through the length of the KEY "Hello" to get the number and then the mod and then giving it a placement in the hash table, not the length of the array. So keep yours keys short. 
#speed is O(1)

index = hashfunc('World', len(hash_table))
hash_table[index] = 'Value for World' #added to the 0 slot.

# the "key" is the input 'Hello' (hashing the key)
# the "value" is what is stored in the array at the index (and then storing the value at the generated index)

#Now, lets retreive the value for "Hello"
index = hashfunc('Hello', len(hash_table))
print(hash_table[index]) #retreives the value for Hello.

print(hash_table) #prints the whole hash tables with all 8 slots.

#-------> #-------> #-------> #-------> #-------> #-------> 

#What if we use 2 words that hash to the same thing? We only have 8 slots.