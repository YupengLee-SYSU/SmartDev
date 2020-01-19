
class BizData:
    def __init__(self):
        self.queryCondition = dict()
        self.selectedField = dict()

    def setDict(self, dict_data):
        self.__dict__ = dict_data