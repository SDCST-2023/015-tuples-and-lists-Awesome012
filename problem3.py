#! python3
"""
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""


input1 = input("input a number: ")
input2 = input("input a number: ")
input3 = input("input a number: ")
input4 = input("input a number: ")
input5 = input("input a number: ")
input6 = input("input a number: ")
input7 = input("input a number: ")
input8 = input("input a number: ")
input9 = input("input a number: ")
input10 = input("input a number: ")

input1 = int(input1)
input2 = int(input2)
input3 = int(input3)
input4 = int(input4)
input5 = int(input5)
input6 = int(input6)
input7 = int(input7)
input8 = int(input8)
input9 = int(input9)
input10 = int(input10)

list = [input1, input2, input3, input4, input5, input6, input7, input8, input9, input10]
nice = -1
if -1 in list:
    cool = list.index(nice)
    del list[cool:]
list.sort()
awesome = list[-1]

print(f"the biggest number you inputed is: {awesome}")