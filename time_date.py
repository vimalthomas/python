#
#programt ot assign date and tim to a tuple.
#time.struct_time(tm_year=2021, tm_mon=5, tm_mday=23, tm_hour=22, tm_min=41, tm_sec=32, tm_wday=6, tm_yday=143, tm_isdst=1)

import time

year,month,mday,hour,minute,second,wday,yday,isdst = time.localtime()

print(year,month,mday,hour,minute,second,wday,yday,isdst)

print(type(year))
