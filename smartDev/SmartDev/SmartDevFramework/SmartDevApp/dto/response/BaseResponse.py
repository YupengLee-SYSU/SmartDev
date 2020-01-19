class BaseResponse:
    def __init__(self):
        self.resultCode = None
        self.resultMsg = None
        self.bizContent = dict()

    def setDict(self, dict_data):
        self.__dict__ = dict_data

