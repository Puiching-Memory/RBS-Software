import requests
import json
from bs4 import BeautifulSoup
import socket
requests.adapters.DEFAULT_RETRIES = 10


def get_address():
    ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    print(ip)
    url = "http://ip138.com/ips138.asp"
    kw2 = {'ip': ip}
    r = requests.request('GET', url, params=kw2)
    r.encoding = 'gbk'
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    soup = soup.ul
    address = soup.contents[0].string[5:]
    address = address.split(' ')[0]
    print(address)
    return address


def Now_weather():
    try:
        result = requests.get(
            url='https://api.seniverse.com/v3/weather/now.json?key=SeKlaz6rgKiOYNaTX&location=guangzhou&language=zh-Hans&unit=c')
        result = result.text

        result = json.loads(result)
        data = result['results']
        data = data[0]
        data = data['location']

        name = data['name']

        data = result['results']
        data = data[0]
        data = data['now']

        temp = data['temperature']
        weater = data['text']

        # print(result)#, result2)
        # print(data)

        now_weater = str(name + ' ' + temp + '° ' + weater)
        #print(name, temp, weater)
        #print(now_weater)
        return now_weater
    except BaseException:
        print('请检查网络链接')
        return 'W:N/A'


def Day3_Weather():
    result2 = requests.get(
        url='https://api.seniverse.com/v3/weather/daily.json?key=SeKlaz6rgKiOYNaTX&location=guangzhou&language=zh-Hans&unit=c&start=-1&days=5')
    result2 = result2.json()

    data = result2['results']
    data = data[0]

    update = data['last_update']
    data = data['daily']
    day1 = data[0]
    day2 = data[1]
    day3 = data[2]
    #---------------------------------------------------------
    date1 = day1['date']
    high1 = day1['high']
    low1 = day1['low']
    rain1 = day1['rainfall']  # 降雨概率
    wind_dire1 = day1['wind_direction']  # 风况(中文)
    wind_deg1 = day1['wind_direction_degree']  # 风向角度
    wind_speed1 = day1['wind_speed']  # 风速
    wind_scale1 = day1['wind_scale']  # 风速等级
    humidity1 = day1['humidity']  # 湿度

    date2 = day2['date']
    high2 = day2['high']
    low2 = day2['low']
    rain2 = day2['rainfall']
    wind_dire2 = day2['wind_direction']
    wind_deg2 = day2['wind_direction_degree']
    wind_speed2 = day2['wind_speed']
    wind_scale2 = day2['wind_scale']
    humidity2 = day2['humidity']

    date3 = day3['date']
    high3 = day3['high']
    low3 = day3['low']
    rain3 = day3['rainfall']
    wind_dire3 = day3['wind_direction']
    wind_deg3 = day3['wind_direction_degree']
    wind_speed3 = day3['wind_speed']
    wind_scale3 = day3['wind_scale']
    humidity3 = day3['humidity']

    # return low3, high3
    # print(data)
    #print(update, day1, high1)
    return date1, date2, date3

if __name__ == "__main__":
    Now_weather()
