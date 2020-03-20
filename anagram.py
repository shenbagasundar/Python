# function to check if two strings are anagram
def anagram(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("The given strings are anagrams")
    else:
        print("The given strings aren't anagrams")

s1 = input("Enter the first string : ")
s1 = s1.upper()
s2 = input("Enter the second string: ")
s2 = s2.upper()
anagram(s1, s2)