def maxnumbers(n):
    lst = []
    for x in range(0, n):
        lst.append(x)
    print(lst)
    print("First max number in the array", max(lst))
    print("First max number in the array", min(lst))
    lst.__delitem__(max(lst))

    print("Second max number in the array", max(lst))


userinput = int(input("Enter number of elements:"))
maxnumbers(userinput)
