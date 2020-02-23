# Function to reverse a string
def reverse(s):
    r = s[::-1]
    if s == r:
        print("Given string is Palindrome")
    else:
        print("Given string is not Palindrome")
reverse("Tat")
reverse("LiriL")
reverse("Malayalam")