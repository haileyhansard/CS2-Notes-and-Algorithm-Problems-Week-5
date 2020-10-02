"""
Things that Hash Tables can be used for:
 - Look something up quickly, FAST SEARCH
 - If you need to look up something quickly, you can use a hash table
 - Usually going to be 0(1) searching, insert, delete
 - Lookup
 - Memoization
 - Count up how many items exist in arrays
 - Transposition tables (mapping alphabet characters to other characters)
 - Access Data quickly by using hash tables
 - Store data using strings (key)


 A set (is same as dictionay but it) doesn't allow duplicates. It's a dictionary with only keys, no values! Just keys. Also uses a hash function under the hood.
 It doesn't allow duplicates because you can't have 2 of the same key in a dictionary.
"""

# Moving out of the guts of creating hash tables, and move into where they would be appropriate. 
# We are going to use python dictionaries {} because it is built in, and we already went over how to create hash table from scratch.

#This is a dictionary is python. AKA hash maps, hash table.
d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

#you can use built in python methods like .get on the d dictionary
print(d.get("foo")) #it prints 12 because thats the value of foo(key)
print(d["foo"]) #prints the value thats in dictionary d at index foo