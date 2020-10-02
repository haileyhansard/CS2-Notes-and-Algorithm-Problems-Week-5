# from my first CS unit test

"""
>>>>>> Variable Types Operators

If different variable types are multipled:
# this will print the string of '123' 3 times
"""
a = 3
b = '123'
print(a*b)


"""
>>>>>> List Combinations	

I have two lists such that each list contains no repeated elements. However, the lists do share some elements, and I want to combine the lists such that no elements are repeated. 
For example, if `list_1` is  `[1,2,4]` and `list_2` is `[1,3,5]`, then the combined list should be `[1,2,4,3,5]`, not `[1,2,4,1,3,5]`. 
Of the choices below, which code will accomplish this? 
*Note: the order of the elements in the resulting list does not matter as long as there are no duplicates.*
"""


"""
>>>>>> Recursive Insertion Sort

Consider this recursive insertion sort algorithm in Python. ```python def insertionSortRecursive(arr,n): # Comment A if ????: return insertionSortRecursive(arr,n-1) last = arr[n-1] j = n-2 while (j>=0 and arr[j]>last): arr[j+1] = arr[j] j = j-1 arr[j+1]=last ``` The base case is missing under `# Comment A`. Which code should replace the question marks?
"""


"""
>>>>>> Overriding Methods Python

Which of the following is the **best** way to implement a `__str__()` method for `Llama`? ```python class Animal: def __init__(self, age, gender): # code not shown class Llama (Animal): def __init__(self, height, is_domesticated): # code not shown def __str__(self): # FILL ME IN ```
"""


"""
>>>>>> Guessing Game
Your friend chooses a random integer between 1 and 32. You decide to use a binary search to guess your friend's number. You agree that, after each guess, your friend will tell you if your guess was greater than, less than, or equal to their number. Which mathematical statement below represents the maximum number of guesses you will need? *Note: All logarithms below are base 2.*
"""

"""
>>>>>> Has An - Relationship

What code replacing the section showing “FILL ME IN” below would establish a “has-a” relationship between the `Book` class and the `Author` class. ```python class Book:     def __init__( self, name, year, author_first, author_last ): self.name = name         self.year = year         self.author = “FILL ME IN”     # class functions would be added here class Author:     def __init__( self, first, last ):     self.first = first         self.last = last     # class functions would be added here ```
"""