
import mysql.connector
#store queries
queries={}

queries['create_table']=('''create table employees.test_name
(name varchar(20),id varchar(20),door_no varchar(20),age varchar(20))''')

queries['insert_test_record']=('''insert into employees.test_name values
('annvita','10','6643','2')


''')
queries['insert_list']=('''insert into employees.test_name values
(%s,%s,%s,%s)
''')

#1) read a file

f = open('data2.txt','r')

lines = [line.rstrip('\n') for line in f]
#print(lines)
words = [word.split(',') for word in lines]
#print(words)
columns = words[0]
print(columns)
rows = words[1:]


#4) create a database connection

try:
    cnx = mysql.connector.connect(user='testuser',password='testpwd',database='employees')
    print('connection is succcessful')
except mysql.connector.Error as err:
    print('connection failed')
    print(err)

#5 create a cursor

cursor=cnx.cursor()



print(queries['create_table'])

try:

    cursor.execute(queries['create_table'])
except mysql.connector.Error as err:
    print('error in creating table')
    print(err)



#6) insert the data into the table

print(queries['insert_test_record'])

try:

    cursor.execute(queries['insert_test_record'])
    print('insert completed')
    cnx.commit()
except mysql.connector.Error as err:
    print('error in inserting test record')
    print(err)

#7 insert a list in the table
print(queries['insert_list'])

for i in rows:
    try:
        cursor.execute(queries['insert_list'],i)
        print('insert completed')
        cnx.commit()
    except mysql.connector.Error as err:
        print('error in inserting record list')
        print(err)
