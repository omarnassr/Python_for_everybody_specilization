'''
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
'''
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
#Loops over lines in handle
for line in fh:
    #strip lines from right-side.
    line.rstrip()
    #List lines into words
    words = line.split()
    #Loops over words
    for i in words:
        if i in lst: #If already in lst keep looping
            continue
        else:
            lst.append(i) #It's not up there append here.

#Sort list and print it            
lst.sort()

print(lst)
