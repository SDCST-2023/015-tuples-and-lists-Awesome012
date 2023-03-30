#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
people = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(people)
input1 = input("input a name from the list ")
input2 = input("input a new name for a replacement ")
if input1 in people: 
    ok = people.index(input1)
    people.remove(input1)
    people.insert(ok,input2)
    print(people)
else:
    print(f"there is no one named {input1} in the list")