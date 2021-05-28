

#parsing mechanism
def parsing_line(line):
    fields =  line.split(',')
    name,room_no,id,town = fields
    return(str(name),int(room_no),int(id),str(town))

line1 = 'vimal, 6643, 34, baton rouge'

print(parsing_line(line1))


#file handling tips
#read a file using file obect.
#there are mode in opening a file. i - normal mode, r- read mode, w- write mode, rb- reading binary, wb - writing binary

def fileopen(filename,mode):
    f = open(filename,mode)
    return f
#Method2 - reads one line at a time
print('use')
for line in fileopen('data2.txt','r'):
    print('method2',line)

#Method1 - reads one line at a time
for line in fileopen('data2.txt','r').readlines():
    print('method1',line)
    line = line.strip()
    for word in line.split(','):
        print(word)

fileopen('data2.txt','r').close()

#always use try and finally after opening the file.

f1 =open('data2.txt','rb')

for line in f1:
    print(line)
