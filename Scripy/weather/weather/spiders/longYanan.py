import scrapy
from weather.items import MysqlConnection
from weather.items import  writerow_csv_file
from weather.items import  read_csv_file
from weather.items import add_data
import time
import datetime
class YananSpider(scrapy.Spider):
    name = 'longyanan'
    start_urls = ['http://www.weather.com.cn/weather/101110300.shtml']
    def parse(self, response):
        station='yanan'
        print_time=time.strftime("%Y-%m-%d %H",time.localtime())
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
                present_time=datetime.datetime.strptime(now_time,'%Y%m%d').date() #time of today
                yesterday_time = present_time - datetime.timedelta(days=1) # yesterday's time
                perfect_time=present_time-datetime.timedelta(days=2)
            elif i==3:                                                      #crontal time
                item0 = item.split(",")
                index_time = item0[0][8:10]
                long_ctime = "%s-%s" % (present_time, index_time)
                perfect_long_time="%s-%s"%(perfect_time,index_time)
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
        time0.reverse()               #order by time
        water.reverse()
        Mysql = MysqlConnection("", "root", "123123", "weatherLog") #connect to mysql on my centent service
        Datalist=Mysql.queryData(station,perfect_long_time)
        for i in range(len(time0)): 
            empty=0
            tuble=(time0[i],)
            if water[i][-1] != "l" and water[1][-1] !="\"":
                if tuble not in Datalist:
                    Mysql.writeTo(station,empty,time0[i],float(water[i]))
                    print("@"*51)
                    print("%s,%s log successfully"%(time0[i],water[i]))
                else:
                    print("%s,%s has already in database"%(time0[i],water[i]))
            else:
                print("%s is an invalid data"%water[i])
        Mysql.closeConnect()
        print("*"*70)
        print("mysql yanan weather log successfully include 24 hours before%s"%print_time)
        print("*" * 70)












