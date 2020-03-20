# Python program to print duplicates from a list of integers
def Duplicate(x):
    length = len(x)
    list =[]
    for i in range(length):
        k = i + 1
        for j in range(k, length):
            if x[i] == x[j] and x[i] not in list:
                list.append(x[i])
    return list

#Sample Input
sample_input =[1,2,2,2]
print(Duplicate(sample_input))