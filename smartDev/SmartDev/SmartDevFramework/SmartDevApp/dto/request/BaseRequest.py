from SmartDevApp.dto.request.BizData import BizData

class BaseRequest:
    def __init__(self):
        # controller
        self.method = None
        # model operation
        self.operation = None
        self.model = None
        self.bizData = BizData()

    def setDict(self, dict_data):
        self.__dict__ = dict_data
