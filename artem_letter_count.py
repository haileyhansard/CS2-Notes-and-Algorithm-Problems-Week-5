"""
Find a way to optimize searching through a string by building a dict as we go.
"""
#Given a string, can we figure out how many times each letter appears in it?
#Case does not matter.
#Spaces don't matter.

#So, we will create a dictionary
def letter_count(s):
    #Dict where keys are letters, and values will be an incrementing counter
    d = {}
    for char in s:
        if char.isspace():
            continue

        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

print(letter_count("aabbc"))
print(letter_count("Hello!"))
print(letter_count("The quick brown fox jumps over the lazy dogs"))

#Now, how would we find which letter appears more than once in a string?
def double_letter(s):
    #d = {} #uncomment this if using the dictionary option
    d = set() #this is using a set, because a set doesn't use a key more than once it will work nicely

    #store letters as keys, and a counter as value
    #looking for all letters, for just the one letter, where value > 1
    for char in s:
        if char.isspace():
            continue

        if char not in d:
            #d[char] = 1
            d.add(char)
        else:
            #d[char] += 1 #uncomment this if using the dictionary option
            return char

    # for key, value in d.items():
    #     if value == 2:
    #         return key

#Runtime is O(n)

print(double_letter("abcdeebf")) #output should be e