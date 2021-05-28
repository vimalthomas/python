
#1) read file into a comprehension generator object

line = (i.rstrip('\n') for i in open("data2.txt","r"))

#2) read line nito generator object after spliting basd on delimiter
field = (s.split(',') for s in line)
columns = next(field)
#create generator
company_dicts = (dict(zip(columns, data)) for data in field)






#3) store the first row as column

#4) zip them based on column name and the values


#5) try to store it into database
