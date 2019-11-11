# list-manupulation-in-python
using split(),sort() and file opening and reading funtions
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
ROMEO.TXT:
"But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief"
SOLUTION
fname = input("Enter the file name: ")
fhand = open(fname)
text = fhand.read()
lst = list()
for line in fhand:
    word = line.rstrip().split()
    for element in word :
        if element in lst:
            continue
        else:
            lst.append(element)
lst.sort()
print(lst)
            
  DESIRED OUTPUT
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
