# Python script to read input from text file and find its index position

with open('D:\Python_word_count.txt') as f:
    for line in f:
        print(line)
        search = line.find('Corona')
        print(search)
