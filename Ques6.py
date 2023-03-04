#6. Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or not?
city_to_find=input("Enter the name of a City to search for :")
def search(filename,word):
    try:
        file=open(filename,"r")
        line_count=0
        for line in file.readlines():
            line=line.strip()
            line_count+=1
            if line==word:
                print("Your City in line No :",line_count)
                break
        else:
            return None
        file.close()
    except FileNotFoundError:
        print("File Not Found")

search('cities.txt',city_to_find)