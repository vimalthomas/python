
import mysql.connector
#store queries
queries={}

queries['create_table']=('''create table employees.test_name2
(name varchar(20))''')

queries['insert_test_record']=('''insert into employees.test_name2 values
('annvita')


''')
queries['insert_list']=('''insert into employees.test_name2 values
(%s)
''')

#1) read a file

f = open('data.txt','r')

lines = (line.rstrip('\n') for line in f)
#print(lines)
words = (word.split(',') for word in lines)
#print(words)
columns = next(words)
print(columns)


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

for i in words:
    try:
        cursor.execute(queries['insert_list'],i)
        print('insert completed')

    except mysql.connector.Error as err:
        print('error in inserting record list')
        print(err)

try:
    cnx.commit()
except mysql.connector.Error as err:
    print('error in committing')
    print(err)
