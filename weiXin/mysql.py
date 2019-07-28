#encoding utf-8
#this file is used to connect with mysql to obtain some weatherData in mysql.
import pymysql
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
    def queryData(self,address,time,):
        prepare_sql="select sum(water) from "+address+" where date >=%s"
        try:
            historyData=self.Mycursor.execute(prepare_sql,(time,))
            boxs=self.Mycursor.fetchall()
            return boxs
        except Exception as e :
            print(e)
    def queryMaxData(self,address,time,):
        prepare_sql="select date,max(water) from "+address+" where date >=%s"
        try:
            historyData=self.Mycursor.execute(prepare_sql,(time,))
            boxs=self.Mycursor.fetchall()
            return boxs
        except Exception as e :
            print(e)




