#5. Write a Python script to append list of city names in a file ‘cities.txt’?
cities_list=["Delhi","Palwal","Ghaziabad","Lucknow","Bhopal","Mumbai"]
file=open('cities.txt','a')
for city in cities_list:
    file.write(city+'\n')
file.close()