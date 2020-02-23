#!/bin/python3
# function to check if two strings are anagram
def check(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("The given strings are anagrams")
    else:
        print("The given strings aren't anagrams")

    # Auto populated input values

s1 = "listen"
s2 = "silent"
check(s1, s2)

#get inputs from user
#s1 = input("Enter first string : ")
#s2 = input ("Enter second string : ")
#check(s1, s2)

#end