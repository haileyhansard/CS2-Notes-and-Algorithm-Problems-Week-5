'''
from leetcode.com/problems/happy-number

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
#UNDERSTAND
#You take each digit of a number, find each digit's square, and add them up. Now you have a new number to repeat the process on. Keep going until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers which end in a 1 are happy numbers.

#ex: the number 19. 
# 1st digit: 1 * 1 = 1
# 2nd digit: 9 * 9 = 81
#sum of those squares = 82
#New number to repeat this process on is 82. If you keep going, you end up at 1. happy.


#PLAN
#Input: An integer (positive)
#Output: True if happy, False, if not happy
#If n transforms to 1, return true
#If n transforms into something we already saw, return false


#EXECUTE
seen_values = set() #create a set to store values in 
def isHappy(self, n):
    if n == 1: #base case is n is equal to 1
        return True 
    #if n was seen before, return False
    if n in self.seen_values:
        return False
    
    #Store the new_sum into a cache
    #We now have "seen" this number before
    self.seen_values.add(n)
    
        #transform n to the new value
        #break up integer into digits
        #turn n into a string
    string_of_digits = str(n)
        #square each digit
    digits_squared = sum([ int(digit)**2 for digit in string_of_digits])
        #sum up all the squares
    return self.isHappy(digits_squared)
