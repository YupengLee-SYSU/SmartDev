from rest_framework.viewsets import ModelViewSet

from SmartDevApp.enums.BaseEnums import resultCode, resultMsg
from SmartDevApp.models import StockBasic
from SmartDevApp.serializers import StockBasicSerializer
from SmartDevApp.dto.response.BaseResponse import BaseResponse as commonResponse
from SmartDevApp.dto.request.BizData import BizData

class ModelViewSetCore(ModelViewSet):
    queryset = StockBasic.objects.all()
    serializer_class = StockBasicSerializer

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
        if bizContent is None:
