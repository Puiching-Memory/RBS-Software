import datetime

utc = datetime.datetime.utcnow()
utc_now = utc
utc = int(utc.strftime("%Y%m%d%H%M%S"))
#utc_now = int(utc_now.strftime("%Y%m%d%H%M%S"))
#print("现在的UTC是：", utc)
utc_FY2 = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
utc_FY2 = utc_FY2.strftime("%H") + '00'

utc = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
utc = int(utc.strftime("%Y%m%d%H%M%S"))
#print("将要获取的UTC小时是：", utc)
print(utc_now)


#get_utc = utc - 4500
get_utc = utc
#print(get_utc)

get_utc = str(get_utc)
get_utc2 = get_utc[0:10]
get_utc = get_utc[10:14]

#print(get_utc)
get_utc = int(get_utc)
    
start_utc = str(get_utc2 + '0000')
print(get_utc2)

utc2_FY2 = get_utc2[0:8]
print(utc2_FY2)
'''
if get_utc < 1500:
    start_utc =  str(get_utc2 + '0000')

elif get_utc < 3000:
    start_utc = str(get_utc2 + '1500')
        
elif get_utc < 4500:
    start_utc = str(get_utc2 + '3000')

else:
    start_utc = str(get_utc2 + '4500')
 '''

#print("UTC起点:", start_utc)
    
final_utc = int(start_utc) + 1459
    
#print("UTC终点:", final_utc)

#return start_utc
    
