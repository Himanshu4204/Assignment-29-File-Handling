#3. Write a Python script to read the above created file ‘myfile.txt’ and display content on the console.?
file=open('myfile.txt','r')
print(file.read())
file.close()
