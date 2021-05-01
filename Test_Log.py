import sys
import os
import sys
import io
import datetime
def create_detail_day():
 '''
 :return:
 '''
 # 年-月-日
 # daytime = datetime.datetime.now().strftime('day'+'%Y-%m-%d')
 # 年_月_日
 daytime = datetime.datetime.now().strftime('day'+'%Y_%m_%d')
 # 时：分：秒
 # hourtime = datetime.datetime.now().strftime("%H:%M:%S")
 # hourtime = datetime.datetime.now().strftime('time' + "%H_%M_%S")
 detail_time = daytime
 # print(daytime + "-" + hourtime)
 # detail_time = daytime + "__" + hourtime
 return detail_time
def make_print_to_file(path='./'):
 '''
  example:
 use make_print_to_file() , and the all the information of funtion print , will be write in to a log file
 :param path: the path to save print information
 :return:
 '''
 class Logger(object):
  def __init__(self, filename="Default.log", path="./"):
   sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
   self.terminal = sys.stdout
   self.log = open(os.path.join(path, filename), "a", encoding='utf8')
  def write(self, message):
   self.terminal.write(message)
   self.log.write(message)
  def flush(self):
   pass
 sys.stdout = Logger(create_detail_day() + '.log', path=path)
 print(create_detail_time().center(60,'*'))
if __name__ == '__main__':
  make_print_to_file(path="/home/log/")
  print('explanation'.center(80, '*'))
  info1 = '从大到小排序'
  info2 = ' sort the form large to small'
  print(info1)
  print(info2)
  print('END: explanation'.center(80, '*'))
