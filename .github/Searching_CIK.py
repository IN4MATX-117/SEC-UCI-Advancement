# query for inserting all the people's name and CIK from SCE 

import mysql.connector
def process_file(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:  # Adjusting encoding here
        return [(line.split(':', 1)[0], line.split(':', 1)[1].strip()) for line in file]

file_path = '/XXX/cik-lookup-data.txt' # path of the cik-lookup-data.txt file
data_for_db = process_file(file_path)

def insert_data(file_path):
    data_for_db = process_file(file_path)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='Search_CIK'
    )
    cursor = connection.cursor()
    cursor.executemany('INSERT INTO CIK_Search (Name, CIK) VALUES (%s, %s)', data_for_db)
    connection.commit()
    connection.close()

file_path = '/Users/christy/Desktop/cik-lookup-data.txt'
insert_data(file_path)

def fetch_cik_by_name(name):
    connection = mysql.connector.connect(
        host='localhost',       
        user='root',             
        password='12345678',    
        database='Search_CIK' 
    )
    cursor = connection.cursor()
    query = "SELECT Name, CIK FROM CIK_Search WHERE Name LIKE %s"
    cursor.execute(query, ('%' + name + '%',))
    records = cursor.fetchall()
    if records:
        for record in records:
            print(record[0],record[1])# Print each CIK
    else:
        print("Nothing find")
    connection.close()

fetch_cik_by_name(name)
