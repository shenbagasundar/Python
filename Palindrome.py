# Function to check Palindrome
def reverse(s):
    s = s.upper()
    r = s[::-1]
    if s == r:
        print("Given string is Palindrome")
    else:
        print("Given string is not Palindrome")


userinput = input("Enter a word to check Palindrome or not:")
reverse(userinput)
