# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.

newArray = []
a = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
for each in a:
    newArray.append(min(each))
    #sum(newArray)
print(sum(newArray))

#----------------------#

# Say you have an array 'prices' for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
"""
U
   (prices) Input: [7,1,5,3,6,4]
   -> 7
P
    loop over range of array 
        set profit variable
        find min (1) and max (6) item out of the rest
        check if next element is higher than i 
            if it is 
                sell
            else
                check the next item
        return profit
E
R
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                profit += (prices[i+1] - prices[i])
        return profit

#----------------------------------#

# Count the number of prime numbers less than a non-negative number, n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""
U
    input n = 10
        There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
    -> 4
P
    def a helper function
        check if i % index is == 0
            if yes then it is NOT a prime
                return False
        return True 
    loop over range(input)
        set counter
        run helper function
        if true increase counter
E
R
"""
class Solution2:
    def helper(self, n):
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        return True
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        counter = 0
        for i in range(2, n):
            print(i, self.helper(i))
            if self.helper(i) == True:
                counter +=1
        return counter

