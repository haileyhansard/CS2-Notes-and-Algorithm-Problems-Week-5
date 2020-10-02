"""
from leetcode.com/problems/jewels-and-stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3


Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""
#UNDERSTAND:
# what are the essentials that the problem is asking us to solve?
# RETURN THE NUMBER of stones that you have that are jewels
# We are looking for each occurrance of any of the chracters in J within the S string
#INPUT: strings
#OUTPUT: a number (of jewels)
#J = types of stones that are jewels
#S = the stones you have

#PLAN:
#count haw many times each character in J appears in S

#NAIVE SOLUTION:
#Double for loop. Loop over one of the strings, then loop over the other string, take each character and compare them.
#For each character in J, 
# compare with each char in S.
    #If charJ = charS, 
    #   count++ 

# Runtime below is n^2 (n squared)
# in this case: n is J, and n is S, so O(J*S)
def numJewelsInStones(self, J: str, S: str):
    count = 0
    for charJ in J:
        for charS in S:
            if charJ == charS:
                count += 1
    return count

       

# We could build a HASH TABLE to make this process easier. 
# Searching in a dictionary is INSTANT. O(1)


#We are searching for: char a
# - does it exist?
# - and how many times?

#Our DICTIONARY will contain:
# keys = char in S 
# value = # of occurrances

def numJewelsHashTableVersion(self, J: str, S: str):
    count = 0

    jewels_dict = {}

    for charJ in J:
        jewels_dict[charJ] = 0 #add each char in J to the jewels dictionary as a key, and set value to 0

    for charS in S: #for each char in S, if it is in jewels dict, then increment it
        if charS in jewels_dict: #O(1)
            count += 1  #now our dictionary will have values incrementing 1, 2, 3 etc
    
    return count
