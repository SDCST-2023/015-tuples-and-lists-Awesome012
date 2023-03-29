#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

input1 = input("say any word: ")
input2 = input("say any other word: ")
input3 = input("say any other word: ")
input4 = input("say any other word: ")
input5 = input("say any other word: ")

awesome = [input1,input2,input3,input4,input5]
print(awesome)