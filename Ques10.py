#10. Write a Python script to extract book data from a bookfile using pickle. Also print extracted book data.?
import pickle

file=open('bookfile.txt','rb')
s=pickle.load(file)
for key in s:
    print(key,':',s[key])
file.close()