from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

class ModelCommon:
    def __init__(self, model=None):
        self.model = model

    def getModelFields(self):
        model = self.getModel()
        fields = model._meta.fields
        # params = [f for f in fields]
        field_data = {}
        for a in fields:
            field_data[a.name] = a.verbose_name
        # print(field_data)
        return field_data

    def setModel(self, model):
        self.model = model

    def getModel(self):
        return self.model

    def queryDataListByPage(self, model_class=None, page_size=None, page_index=None):
        if model_class is None:
            model_class = self.model
        data = model_class.objects.all()
        paginator = Paginator(data, page_size)
        page_count = paginator.num_pages
        data_list = []
        if page_count > 0:
            if page_index is not None:
                for i in range(page_count):
                    data_list.append(json.loads(serializers.serialize("json", paginator.page(i+1))))
            else:
                data_list.append(json.loads(serializers.serialize("json", paginator.page(page_index))))
        return data_list

    def insertDataList(self, data_dict_list=None, model_class=None):
        model_list = []
        if data_dict_list is not None and model_class is not None:
            for data_dict in data_dict_list:
                tmp_model = model_class()
                for field in data_dict_list[0].keys():
                    setattr(tmp_model, field, data_dict[field])
                model_list.append(tmp_model)
        model_class.objects.bulk_create(model_list)