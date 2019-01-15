import quandl
import os

#'NSE/INFY'


class Stock_Table():
    def __init__(self,path,table,date):
        if not date:            
            import datetime
            now = datetime.datetime.now()
            date = {'start':'2000-01-01','end':now.year+'-'+now.month+'-'+now.day}
        quandl.read_key(filename=path)
        self.data = quandl.get(table,start_date = date['start'],end_date = date['end'])


table = Stock_Table(path="key/key",table='NSE/INFY', date = { 'start': '2016-01-01', 'end': '2019-12-31' })

x=table.data