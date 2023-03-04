#1. Write a Python script to print the following status of a file:
#    b. Whether a file is closed or not
#    c. Which file opening mode is used
#    a. Whether a file is read only
#    d. Name of the file
file=open('Example.txt','r')

print("File closed Status :",file.closed)
print("File opening Mode :",file.mode)
print("File name:",file.name)
print("File Read Only Status:",file.readable())

file.close()
