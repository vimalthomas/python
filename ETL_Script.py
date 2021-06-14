def loadfile(filename,delimiter):
    bufsize = 65536
    with open(filename) as infile:
        words=[]
        while True:
            lines = infile.readlines(bufsize)
            if not lines:
                break
            lines_striped = [line.rstrip("\n") for line in lines]
            #words = [word.split(",") for word in lines_striped]
            for word in lines_striped:
                words.append(word.split(","))

        return words


def header_data_split(collection):
    header = collection[0]
    return(header)



def data_profiling(header,row):
    unique_collection,index_collection = {},{}

    for index,value in enumerate(header):
        column_values = set()
        for i in rows:
            val = i[index]
            if val not in column_values:
                column_values.add(val)


        unique_collection[value]=column_values
        index_collection[value]=index
    return ([unique_collection,index_collection])

def like_by_gender(header,row,index_dict):
    get_gender_index=index_dict['gender']
    get_likes_received_index=index_dict['likes_received']
    get_mobile_likes_received_index=index_dict['mobile_likes_received']
    get_www_likes_received_index=index_dict['www_likes_received']

    neutral_likes,male_likes,female_likes=[],[],[]
    for i in row:
        if i[get_gender_index]=='male':
            male_likes.append(int(i[get_likes_received_index]))
            male_likes.append(int(i[get_mobile_likes_received_index]))
            male_likes.append(int(i[get_www_likes_received_index]))
        elif i[get_gender_index]=='female':
            female_likes.append(int(i[get_likes_received_index]))
            female_likes.append(int(i[get_mobile_likes_received_index]))
            female_likes.append(int(i[get_www_likes_received_index]))
        else:
            neutral_likes.append(int(i[get_likes_received_index]))
            neutral_likes.append(int(i[get_mobile_likes_received_index]))
            neutral_likes.append(int(i[get_www_likes_received_index]))

    return((sum(male_likes),sum(female_likes),sum(neutral_likes),))


def like_platform(header,row,index_dict):
    get_id_index=index_dict['userid']
    common_user,mobile_user,web_user=set(),set(),set()

    get_likes_received_index=index_dict['likes_received']
    get_mobile_likes_received_index=index_dict['mobile_likes_received']
    get_www_likes_received_index=index_dict['www_likes_received']

    for i in row:
        if int(i[get_likes_received_index])>0:
            common_user.add(i[get_id_index])

        if int(i[get_mobile_likes_received_index])>0:
            mobile_user.add(i[get_id_index])

        if int(i[get_www_likes_received_index])>0:
            web_user.add(i[get_id_index])

    return((common_user,mobile_user,web_user))

""" File Loading """
#Open a file and store it in the memory
rows=loadfile('pseudo_facebook.csv',',')


""" Header and Row Creation """
#create rows and columns
column_names = header_data_split(rows)
rows.pop(0)

"""DATA PROFILING"""
profiling_results = data_profiling(column_names,rows)

for i,j in profiling_results[0].items():
    if i=='userid':
        print(len(j))


"""UNIQUE DATA COLLECTION"""
print('total record count is ',len(rows))

"""find out the following questions using sets"""

"""1) who has more likes, male or female?"""
like_results = like_by_gender(column_names,rows,profiling_results[1])

print('total likes for males',like_results[0])

print('total likes for females',like_results[1])

print('total likes for Unknow Gender',like_results[2])

"""2) whch user has more friends?"""



"""3) which age group has more friends?

4) how many users have only mobile likes?
"""

platform_results = like_platform(column_names,rows,profiling_results[1])

print("count of common platform users",len(platform_results[0]))

print("count of mobile platform users",len(platform_results[1]))

print("count of web platform users",len(platform_results[2]))

print("count of only mobile users",
len(platform_results[1] - platform_results[2] ))

print("count of only web users",
len(platform_results[2] - platform_results[1] ))

#perform data cleansing

# estabilish a connection

# Insert data into staging table

#Perform deduping

#Select queries

#Load into final table
