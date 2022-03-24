import requests
import mysql.connector

# fetching the data using request module from api
api = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
data = api.json()


# 1st way:-  storing data into 2D array
def fetchApi():
    outer_list = []
    
    # runing  loop over fetch data
    for i in data:
        for x in data[i]:
            inner_list = []
            if 'Nation'  in x:
                inner_list.append(x['Nation'])
                
            if 'Year' in x:
                inner_list.append(x['Year'])
                
            if "Population" in x:
                inner_list.append(x["Population"])
                
            outer_list.append(inner_list)
    return  outer_list             
              
print(fetchApi())
    
    

# 2nd way :-Storing data in tabular format

# connecting with mysql  database
mydb = mysql.connector.connect(
    host ='localhost',
    user ='root', 
    password = 'Megha@8287',
    database = 'FINAL_PROJECT')

# creating cursor
mycursor = mydb.cursor()

# creating database
mycursor.execute('CREATE DATABASE FINAL_PROJECT')

# Creating  table for storing data
mycursor.execute('CREATE TABLE DATA(Country VARCHAR(80),Year integer,Population integer)')

nation = []
year = []
population = []

def fetch_data():
    
    # runing  loop over fetch data
    for i in data:
        for x in data[i]:
            if 'Nation'  in x:
                nation.append(x['Nation'])
                
            if 'Year' in x:
                year.append(x['Year'])
                
            if "Population" in x:
                population.append(x["Population"])
                
    index = 0
    while index < len(nation):
        sql = 'INSERT INTO DATA(Country,Year,Population) VALUES(%s,%s,%s)'
        val = (nation[index],year[index],population[index])
        mycursor.execute(sql,val)
        
        # commiting all the  changes into Data table
        mydb.commit()
        print(mycursor.rowcount, "Record inserted successfully into DATA table")
        
        index+=1
              
              
fetch_data()
    