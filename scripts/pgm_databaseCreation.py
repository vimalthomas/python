import mysql.connector

#connection creation

try:
  cnx = mysql.connector.connect(user='testuser',password='testpwd',host='localhost',database='employees')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

DB_Name = 'employees'

QUERIES = {}

QUERIES['CREATE_EMP']=(
    "CREATE TABLE employees.`sample_employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`))")

QUERIES['INSERT_EMP']=(
    "INSERT INTO employees.`sample_employees`"
    "values(%s,%s,%s,%s,%s,%s)")




cnx = mysql.connector.connect(user='testuser',password='testpwd')
cursor = cnx.cursor()

#Creating tables.

for tablename,tabledesc in QUERIES.items():
    if (tablename=='CREATE_EMP' ):

        print('table {} is being created' .format(tablename))
        print(tabledesc)
        try:
            cursor.execute(tabledesc)
        except mysql.connector.Error as err:
            print('error in creating table')
            print(err.msg)
    elif(tablename=='INSERT_EMP'):
        print('insert query')
        try:
            #cursor.execute(tabledesc,('10','2020-01-01','','','M','2020-01-01'))
            cursor.execute(tabledesc,['11','2020-01-01','','','M','2020-01-01'])
            #cursor.execute(tabledesc,{'emp_no':'11','birth_date':'2020-01-01','first_name':'vimal','last_name':'thomas','gender':'M','hire_date':'2020-01-01',})
        except mysql.connector.Error as err:
            print('error in inserting values')
            print(err.msg)
cnx.commit()
cursor.close()
cnx.close()
