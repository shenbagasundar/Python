# Python script to reverse a string

# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string

s = "Tamil"

print("The original string  is : ", s)
print("The reversed string(using extended slice syntax) is : ", reverse(s))
