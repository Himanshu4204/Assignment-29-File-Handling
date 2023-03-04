#9. Write a Python script to store book data in a file. Book data is in the form of a dictionary in which book name is the key 
#    and price is its value. Use pickle to store data into a file (say bookfile)
import pickle

Book_data={"English":256,"Math":300,"Hindi":190,"Science":400,"Physical":100}
file=open('bookfile.txt','ab')
pickle.dump(Book_data,file)
file.close()
