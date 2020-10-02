hash_table = [None] * 8 #8 slots, all initialized to None

def my_hash(string): #gets the hash
    #take every character in the string and convert to number
    string_utf = string.encode()
    total = 0
    for char in string_utf:
        total += char 
        #limit total to 32 bits
        total &= 0xffffffff
    return total

def hash_index(key): #gets the index
    hash_num = my_hash(key)
    return hash_num % len(hash_table)

def put(key, val):
    #hash the key and get an index
    i = hash_index(key)
    #check if something already exists at that index
    if hash_table[i] != None:
        print(f"Collision! Overwriting {repr(hash_table[i])}")
        #store the value in the array at the hashed index
    hash_table[i] = val

def get(key):
    #hash the key and get an index
    i = hash_index(key)
    #return the value from the array at that index
    return hash_table[i]


put("Hello", "Hello Value") #key, value, will be put into the index position that it hashes to (4)
put("World", "World Value") #key, value, will be put into the index position that it hashes to (0)

print(hash_table)

put("foo", "Foo Value")
print(hash_table)

put("Name", "Hailey")
print(hash_table)

print(hash_index("Hello")) #4 will print
print(hash_index("foo"))   #4