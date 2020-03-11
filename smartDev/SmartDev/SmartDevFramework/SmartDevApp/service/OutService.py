import SmartDevApp.util.commonUtils as commonUtils
import tushare as ts
import SmartDevApp.util.dataframeUtils as dataframeUtils

class OutService:
    def __init__(self):
        self.token = commonUtils.getToken()
        self.ts = ts

    def getStockBasicData(self, fields):
        field_str = ""
        for i in range(len(fields)):
            if i != len(fields)-1:
                field_str = field_str + fields[i] + ","
            else:
                field_str = field_str + fields[i]
        self.ts.set_token(self.token)
        pro = self.ts.pro_api()
        frame_data = pro.query('stock_basic', exchange='', list_status='L', fields=field_str)
        data_list = dataframeUtils.dataframeToDictlist(frame_data)
        return data_list

    def getDailyLineData(self, stock_code, start_date, end_date):
        pro = self.ts.pro_api()
        frame_data = pro.daily(ts_code=stock_code, start_date=start_date, end_date=end_date)
        data_list = dataframeUtils.dataframeToDictlist(frame_data)
        return data_list