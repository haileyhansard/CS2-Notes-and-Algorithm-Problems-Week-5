"""
Index: Find a way to search through rows of data that isn't easy to search through, and find ways to group data in better ways.
"""

records = [
    ("Alice", "Engineering"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Sarah", "Sales"),
    ("Pranjal", "Sales"),
    ("Grace", "Marketing"),
    ("Charles", "Marketing"),
    ("Brian", "Marketing"),
    ("Jordan", "Marketing"),
]

#Proposed Dictionary
#Keys will be departments
#values array of names, or list of names

#what we know = dept(keys). what we want to know = names(values)

def build_index(recs):
    index = {} #empty dictionary

    for record in recs:
        name, dept = record #first var will be name, 2nd var will be dept
        
        #Check if dept is already in index
        if dept in index:
            #If it is, add name to the list
            index[dept].append(name)
        else:
            #Else, create new key with list with the name in it
            index[dept] = [name]
    return index
    #Runtime of building this index is O(n)


department_index = build_index(records)
print(department_index) #so that you can see the dictionary you built

#print all the departments
print(department_index.keys())

#print everyone in Engineering:
print(department_index['Engineering'])

#print everyone in Sales:
print(department_index['Sales'])

#print everyone in Marketing:
print(department_index['Marketing'])
