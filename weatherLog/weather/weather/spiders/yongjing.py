# -*- coding: utf-8 -*-

import scrapy
from weather.items import  writerow_csv_file
from weather.items import  read_csv_file
from weather.items import add_data
import time
import datetime
class YananSpider(scrapy.Spider):

    name = 'yj'
    start_urls = ['http://www.weather.com.cn/weather/101161103.shtml']
    def parse(self, response):
        standSet=[]
        stand_csv = read_csv_file("/home/mayuri/python/weather_log/dataLogCsv/yongjing.csv")
        for i in stand_csv:
           standSet.append(i[0])
        print_time=time.strftime("%Y-%m-%d %H",time.localtime())
        time_water = []
        time0 = []
        water = []
        temp = response.xpath("//script/text()").extract()
        temp1=None
        temp2=None
        temp1=temp[1]  
        temp2=temp1.strip()
        temp3=temp2.split("{") 
        for i,item in enumerate(temp3):
            if i==2:
                now_time=item[7:15]
                present_time=datetime.datetime.strptime(now_time,'%Y%m%d').date() 
                yesterday_time = present_time - datetime.timedelta(days=1)  
            elif i==3:                                                      
                item0 = item.split(",")
                index_time = item0[0][8:10]
                long_ctime = "%s-%s" % (present_time, index_time)
                time0.append(long_ctime)
                water_content = item0[5][8:11]
                s_water_content=add_data(water_content)
                water.append(s_water_content)
            elif i>3 and i<27:                                          
                item4=item.split(",")
                ctime=item4[0][8:10]
                if int(ctime)>=int(index_time):
                    long_ctime="%s-%s"%(yesterday_time,ctime)    
                    time0.append(long_ctime)                 
                    water_content = item4[5][8:11]
                    s_water_content=add_data(water_content)                         
                    water.append(s_water_content)
                else:
                    long_ctime = "%s-%s" % (present_time, ctime)    
                    time0.append(long_ctime)
                    water_content=item4[5][8:11]
                    s_water_content=add_data(water_content)
                    water.append(s_water_content)
        time0.reverse()               
        water.reverse()
        for i in range(len(time0)): 
            data=[]
            data.append(time0[i])
            data.append(water[i])
            if data[1][-1] !="l" and data [1][-1]!="\"":
                if data[0] not in standSet:
                    writerow_csv_file("/home/mayuri/python/weather_log/dataLogCsv/yongjing.csv",data)
                else:
                    print("%s exists"%data)
            else:
                print("%s is an invalid data"%data)
        print("*"*70)
        print("yongjing weather log successfully include 24 hours before%s"%print_time)
        print("*" * 70)












