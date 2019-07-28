#encoding=utf-8
import datetime 
from mysql import MysqlConnection
class Text(object):
	def __init__(self):
		pass
	def getText(self):
		return """    宝塔建于唐代，高44米，共九层，登上塔顶，全城风貌可尽收眼底。它是历史名城延安的标志，是革命圣地的象征，是延安市的标志性建筑，是游览延安的必去之地。
山下还有历代遗留下来的摩岩刻字多处，范仲淹隶书的“嘉岭山”和“胸中自有数万甲兵”等题刻最著名。宝塔山融自然景观、人文景观、历史文物、革命旧址为一体的著名风景名胜区。
宝塔山，古称丰林山，宋时改名为嘉岭山。现在人们又称宝塔山。位于延安城东南方，海拔1135.5米，为周围群山之冠。宝塔山上视野开阔，林木茂盛，山林空气清新，凉爽宜人，夏季平
均气温较内低3～4摄氏度，是消夏避暑的好地方 [1]  。宝塔建于唐代，高44米，共九层，登上塔顶，全城风貌可尽收眼底。它是历史名城延安的标志，是革命圣地的象征。在塔旁边有一口明
代铸造的铁钟，中共中央在延安时，曾用它来报时和报警。此外山上还有长达260米的摩崖石刻群和碑石刻岸面整齐，岸石完整，是难得的石刻艺术。山上现已建成为宝塔山公园，林木葱郁，
环境优美。宝塔山是延安市的标志性建筑，是游览延安的必去之地。
                """
	def getWeather(self,addr):
		myMysql=MysqlConnection("","root","123123","weatherLog")
		present_time=datetime.datetime.today()
		yesterday=present_time-datetime.timedelta(days=7)
		query_time=datetime.datetime.strftime(yesterday,"%Y-%m-%d-%H")
		Data_list=myMysql.queryData(addr,query_time)
		maxWater=myMysql.queryMaxData(addr,query_time)
		myMysql.closeConnect()
		sum_water=Data_list[0][0]
		if sum_water>0:
			waterMsg="延安市过去一周的降雨量为：%.2fmm,其中在%s日%s时降雨量达到：%smm/每小时"%(sum_water,maxWater[0][0][0:10],maxWater[0][0][11:],maxWater[0][1])
		else :
			waterMsg="延安市过去一周内没有降雨"
		return waterMsg
		
if __name__=="__main__":
	myText=Text()
	myText.getWeather("yanan")
	
	
		
	

