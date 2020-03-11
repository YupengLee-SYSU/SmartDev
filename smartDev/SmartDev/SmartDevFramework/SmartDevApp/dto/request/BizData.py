
class BizData:
    def __init__(self, dict_data=None):
        self.queryCondition = dict()
        self.selectedField = dict()
        if dict_data is not None:
            self.setDict(dict_data)

    def setDict(self, dict_data):
        self.__dict__ = dict_data