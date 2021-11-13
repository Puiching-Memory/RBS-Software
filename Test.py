# coding=utf-8
"""编写时间：2019.2.14"""
 
"""
思路：1、用户输入时间
      2、获取当前时间
      3、根据两个时间判断还剩多少秒关机
      4、使用shutdown -s -t xxx关机
      5、使用shutdown -a取消关机
"""
 
import sys,os,time,datetime
#os.system("echo 你好".encode('utf-8').decode('gbk'))
print("使用说明：按要求输入关机时间")
 
'''获取关机时间'''
input_time_hourandoff =input('请输入小时(如果需要关机，输入 取消关机)：')
if input_time_hourandoff == "取消关机":
    if os.system("shutdown -a") ==1116:
        print("因为没有任何进行中的关机过程，所以无法中止系统关机。(1116)")
    else:
        print("取消成功")
else:
    input_time_hour = int(input_time_hourandoff)
    input_time_minute = int(input('请输入分钟：'))
 
    '''检查输入数据格式，暂无'''
 
    '''获取当前时分秒'''
    curtime = datetime.datetime.now()
    curtime_hour = curtime.hour
    curtime_minute = curtime.minute
 
    '''计算秒数,先换算成时再相减'''
    hours = ((input_time_hour + (input_time_minute / 60)) - (curtime_hour + curtime_minute / 60))
    minutes = hours * 60
    seconds = hours * 60 * 60
    print("距离关机还有%d分钟"%minutes)
    os.system('shutdown -s -t %d' % seconds)
    print("设置成功，如果想取消关机，打开程序输入：取消关机 即可")