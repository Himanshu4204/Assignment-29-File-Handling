#2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.?
file=open('myfile.txt','w')
file.write(input("Enter your text:"))
file.close()