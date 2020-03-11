from rest_framework.viewsets import ModelViewSet

from SmartDevApp.enums.BaseEnums import resultCode, resultMsg
from SmartDevApp.models import StockBasic
from SmartDevApp.models import DailyLine
from SmartDevApp.serializers import StockBasicSerializer
from SmartDevApp.serializers import DailyLineSerializer
from SmartDevApp.dto.response.BaseResponse import BaseResponse as commonResponse
from SmartDevApp.dto.request.BizData import BizData
from SmartDevCore.ModelCommon import ModelCommon
from SmartDevApp.service.OutService import OutService
from rest_framework import serializers

class StockBasicViewSetCore(ModelViewSet, ModelCommon):
    queryset = StockBasic.objects.all()
    serializer_class = StockBasicSerializer

    def fileProcTest(self, bizContent):
        self.setModel(StockBasic)
        data_obj_list = self.queryDataListByPage(page_size=5, page_index=1)
        print("query result, data size:"+str(len(data_obj_list)))
        response = commonResponse()
        response.resultCode = resultCode.SUCCESS
        response.resultMsg = resultMsg.SUCCESS
        response.bizContent = ""
        return response

    def queryByCondition(self, bizContent):
        bizData = BizData()
        bizData.setDict(bizContent)
        print("queryset:"+str(bizData.queryCondition))
        print("selectedField:"+bizData.selectedField)

        self.queryset = StockBasic.objects.filter(ts_code=bizData.queryCondition.get("ts_code"))

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        respData = serializer.data

        response = commonResponse()
        response.resultCode = resultCode.SUCCESS
        response.resultMsg = resultMsg.SUCCESS
        response.bizContent = str(respData)
        return response

    def updateByCondition(self, bizContent):
        self.setModel(StockBasic)
        data = []
        fields = self.getModelFields()
        print(bizContent)
        bizData = BizData(dict_data=bizContent)
        if len(bizData.selectedField) == 0:
            # update all the stock base infomation
            fields = [f for f in fields if f not in self.getExcludeParams()]
            outService = OutService()
            data = outService.getStockBasicData(fields)
        else:
            pass
        self.insertBatchData(data_dict_list=data)
        response = commonResponse()
        response.resultCode = resultCode.SUCCESS
        response.resultMsg = resultMsg.SUCCESS
        response.bizContent = str(data)
        return response

    def getExcludeParams(self):
        return ['index']

    def insertBatchData(self, data_dict_list=None):
        model_list = []
        if data_dict_list is not None:
            for data_dict in data_dict_list:
                tmp_model = StockBasic()
                for field in data_dict_list[0].keys():
                    setattr(tmp_model, field, data_dict[field])
                model_list.append(tmp_model)
        StockBasic.objects.bulk_create(model_list)

class DailyLineViewSetCore(ModelViewSet, ModelCommon):
    queryset = DailyLine.objects.all()
    serializer_class = DailyLineSerializer

    def updateByCondition(self, bizContent):
        self.setModel(DailyLine)
        data = []
        # fields = self.getModelFields()
        print(bizContent)
        bizData = BizData(dict_data=bizContent)
        if len(bizData.selectedField) == 0:
            # stock_code_list = self.getStockCode()
            # test_stock_code = "000001.SZ"
            data_list = []
            stock_code_list = self.getStockCode()
            for stock_code in stock_code_list:
                start_date = "20100101"
                end_date = "20200215"
                outService = OutService()
                data_list = outService.getDailyLineData(stock_code=stock_code, start_date=start_date, end_date=end_date)
                self.insertDataList(data_dict_list=data_list, model_class=DailyLine)
                print("finished stock_code:"+stock_code)
        else:
            pass
        response = commonResponse()
        response.resultCode = resultCode.SUCCESS
        response.resultMsg = resultMsg.SUCCESS
        response.bizContent = str(data)
        return response

    def getStockCode(self):
        queryset = StockBasic.objects.all()
        stock_code_list = []
        for stock_value in queryset.values_list():
            stock_code_list.append(stock_value[1])
        return stock_code_list

