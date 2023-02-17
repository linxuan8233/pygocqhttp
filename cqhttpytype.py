"""
PYCQHTTP 类库
"""
import json
try:
    from . import Error
except ImportError:
    import Error
class Array:
    def __init__(self, data):
        if type(data) == list or type(data) == tuple:
            self.data = list(data)
        else:
            raise Error.CQTypeError("该数据似乎不是Python中的数组")
    def __str__(self):
        "给列表或者元组加上转成字符串"
        return str(tuple(self.data))
    def __list__(self):
        "给列表或者元组加上转成列表"
        return list(self.data)
    def __tuple__(self):
        "给列表或者元组加上转成元组"
        return tuple(self.data)
    def __len__(self):
        "返回长度"
        return len(self.data)
    def __getitem__(self, key):
        "返回索引"
        return self.data[key]
    def __add__(self, other):
        "加"
        if type(other) == list or type(other) == tuple or type(other) == Array:
            return self.data + other
        else:
            raise Error.CQTypeError("类型不能相加")
    def __sub__(self, other):
        "减"
        if type(other) == list or type(other) == tuple or type(other) == Array:
            return self.data - other
        else:
            raise Error.CQTypeError("类型不能相减")
    def __mul__(self, other):
        "乘"
        if type(other) == int:
            return self.data * other
        else:
            raise Error.CQTypeError("类型不能相乘")
    def __iter__(self):
        "迭代器"
        return iter(self.data)
    def __contains__(self, item):
        "是否包含"
        return item in self.data
    def __reversed__(self):
        "反转"
        return reversed(self.data)
    def append(self, item):
        "添加"
        self.data.append(item)
    def pop(self, index):
        "删除"
        return self.data.pop(index)
    def remove(self, item):
        "删除"
        self.data.remove(item)
    def clear(self):
        "清空"
        self.data.clear()
    def index(self, item):
        "索引"
        return self.data.index(item)
    def count(self, item):
        "计数"
        return self.data.count(item)
    def sort(self, key=None, reverse=False):
        "排序"
        self.data.sort(key=key, reverse=reverse)
    def reverse(self):
        "反转"
        self.data.reverse()
    def copy(self):
        "复制"
        return Array(self.data.copy())
class Received:
    #设置下通用属性
    time: int #时间戳
    self_id: int #机器人QQ
    post_type: str #上报类型

    def __init__(self, data):
        "解析收到的消息并提取信息"
        self.data = data
        #设置内部字典
        self.__dict__ = {}
        #将字符串转成字典
        #判断这玩意到底是啥类型
        if type(data) == str:
            self.__dict__ = json.loads(data)
        elif type(data) == dict:
            self.__dict__ = data
    def __repr__(self) -> str:
        #设置对象信息
        return f"Received({self.__dict__})"
    #设置调用属性返回信息
    def __getattr__(self, name):
        #如果遇到套娃的就递归一下
        if type(self.__dict__.get(name)) == dict:
            return Received(self.__dict__.get(name))
        else:
            return self.__dict__.get(name)
    #设置访问属性返回信息
    def __getitem__(self, name):
        #如果遇到套娃的就递归一下
        if type(self.__dict__.get(name)) == dict:
            return Received(self.__dict__.get(name))
        #否则直接返回就行
        else:
            return self.__dict__.get(name)
    
