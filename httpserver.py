"""
触发器-HTTP服务器 模块
LX 2023
Linxuan@lxdn.cc
"""
#导包
from flask import Flask, request, jsonify
import threading,datetime
try :
    from . import Cqcode, Error,cqhttpytype
except ImportError:
    import Cqcode, Error,cqhttpytype
#定义一个装饰器函数 使被装饰的函数在一个新的线程中运行
def run_in_thread(func):
    def wrapper(*args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.start()
    return wrapper
#定义一个触发器类
class Trigger:
    def __init__(self,app,host,port,path="/") -> None:
        self.trigger = {}#触发器字典
        self.type=[
            "group",
            "private",
            "notice",
            "friend_recall",
            "group_recall",
            "group_upload",
            "group_admin",
            "group_decrease",
            "group_increase",
            "group_ban",
            "friend_add",
            "group_name",
            "group_card",
            "group_leave",
            "group_special_title",
            "group_poke",
            "group_honor",
            "friend_poke",
            "client_status",
            "essence",
            "heartbeat","**"
            ]
        self.app=app
        self.host=host
        self.port=port
        if self.path==" "or self.path=="":
            self.path="/"#默认路径
        else:
            self.path=path
    def on_message(self,*args, **kwargs):
        def wrapper(func):
            def run(*arg, **kwarg):
                #判断触发器类型
                if args[0] in self.type:
                    ...
                else:
                    raise Error.HttpTypeError("触发器类型错误")
    #设置内部解析函数
    def _parse(self,data):
        #先空着
        ...
    #启动HTTP服务器
    def run(self):
        #先设置一个路由接受json数据
        @self.app.route(self.path,methods=['POST'])
        def index():
            #解析json数据
            data=request.get_json()
            #发送到内部解析函数
            self._parse(data)
            #返回一个空字符串防止go-cqhttp报错
            return "",200
        self.app.run(host=self.host,port=self.port)
#定义flask类
def new(name,host:str=None,port:int=None,path="/") -> Trigger:
    app=Flask(name)
    trigger=Trigger(app,host,port,path)
