# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import csv
import pymysql
class WeatherScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def read_csv_file(path):           
    temp=[]
    with open(path,"r") as fd:
        read_file=csv.reader(fd)
        for i in read_file:
            temp.append(list(i))
    return temp

def writerow_csv_file(path,data):          
    with open (path,"a+",newline="") as fd: 
        csv_file=csv.writer(fd)
        csv_file.writerow(data)
        print("@" * 70)
        print("log %s successfully"%data)
        print("@"*70)
def add_data(data):
    re_data=data
    return re_data
class MysqlConnection():
    def __init__(self,addr,user,passwd,database):
        self.addr=addr
        self.user=user
        self.passwd=passwd
        self.database=database
        try:
            self.Myconnection = pymysql.connect(self.addr, self.user, self.passwd, self.database)
            self.Mycursor = self.Myconnection.cursor()
        except Exception as e:
            print(e)
    def writeTo(self,address,Id,Date,Water):
        sql="insert into "+address+ " values(%s,%s,%s)" # when add two str becare there alaway make "" in it  ,this is not we hope;
        try:
            self.Mycursor.execute(sql,(Id,Date,Water,))
        except Exception as e:
            print(e)
        self.Myconnection.commit()
    def closeConnect(self):
        self.Mycursor.close()
        self.Myconnection.close()
        print("connection has shutdwon  ")
    def queryData(self,address,time,):
        prepare_sql="select date from "+address+" where date >=%s"
        try:
            historyData=self.Mycursor.execute(prepare_sql,(time,))
            boxs=self.Mycursor.fetchall()
            return boxs
        except Exception as e :
            print(e)




