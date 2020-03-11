from django.shortcuts import render
from .dto.request.BaseRequest import BaseRequest as commonRequest
from .dto.response.BaseResponse import BaseResponse as commonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSetMixin
from .models import StockBasic
from .serializers import StockBasicSerializer
# from .service import StockBasicService
from django.http import HttpRequest
from django.http import HttpResponse
import tushare as ts
from django.views.generic import View
import json
from SmartDevCore.ModelCore import StockBasicViewSetCore

class StockBasicViewTest(StockBasicViewSetCore):
    def Main(self, request):
        requestContent = request.body
        request_json = json.loads(requestContent)
        baseRequest = commonRequest()
        baseRequest.setDict(request_json)
        controller = getattr(self, baseRequest.method)
        baseResponse = controller(baseRequest.bizData)
        return HttpResponse(json.dumps(baseResponse.bizContent, default=lambda o: o.__dict__, sort_keys=True, indent=4))