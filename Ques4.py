# 4. Write a Python script to store a list of city names in a file ‘cities.txt’?
cities_list=["Faridabad","Gurgoan","Noida","Jaipur","Bhopal","Nagpur"]
file=open('cities.txt','w')
for city in cities_list:
    file.write(city+'\n')
file.close()