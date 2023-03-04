#7. Write a Python script to count the number of Python keywords occurring in a python source file.?
import keyword

file=open('Ques6.py','r')

source_code=file.read()
words=source_code.split()
keyword_count=0

for word in words:
    if keyword.iskeyword(word):
        keyword_count+=1

print("Total Number of Keyword found in this source file",keyword_count)

file.close()