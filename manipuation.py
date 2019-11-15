
fname = input("Enter the file:")
fh = open(fname)
 for line in fh :
     line = line.rstrip()
     if not line.stratswith('from') : continue
     words = line.split()
print(words[1])
