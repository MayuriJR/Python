import datetime
present_time=datetime.datetime.today()
query_time=present_time-datetime.timedelta(days=2)
str_time=datetime.datetime.strftime(query_time,"%M-%m-%d-%H")
