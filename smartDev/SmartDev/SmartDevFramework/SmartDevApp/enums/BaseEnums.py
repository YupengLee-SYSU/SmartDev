from enum import Enum


class operation(Enum):
    QUERY = "query"
    ADD = "add"
    DELETE = "delete"
    UPDATE = "update"


class model(Enum):
    STOCKBASIC = "StockBasic"
    KDAYLINE = "KdayLine"


class resultCode(Enum):
    SUCCESS = "000"
    FAIL = "001"


class resultMsg(Enum):
    SUCCESS = "success"
    FAIL = "fail"