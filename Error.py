"""
PyGo-Cqhttp 错误类型
LX 2022
linxuan@lxdn.cc
"""
class CqError(Exception):
    def __init__(self,n):
        self.n = n
class HttpError(Exception):
    def __init__(self,n):
        self.n = n
class HttpServerError(Exception):
    def __init__(self,n):
        self.n = n
class HttpDataError(Exception):
    def __init__(self,n):
        self.n = n
class CQTypeError(Exception):
    def __init__(self,n):
        self.n = n
class HttpTypeError(Exception):
    def __init__(self,n):
        self.n = n