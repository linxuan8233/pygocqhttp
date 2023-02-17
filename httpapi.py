"""
PyGo-Cqhttp 正向httpapi基础函数库
Lx c2022
Linxuan@lxdn.cc
"""
from typing import Any
import requests,json
from html import unescape


class cqbotapiError(Exception):
    def __init__(self,n):
        self.n=n
class cqbotapi():
    r"""内部封装go-cqhttp httpapi接口函数同时封装cq码 封装了cq码与字典的互转函数"""
    def __init__(self,host:str,port:int) -> None:
        self.port = int(port)
        self.host = host
    def network(self,url,data="",method="GET") -> requests.Response:
        if method == "GET":
            return requests.get(url,data=data)
        else:
            return requests.post(url,data=data)
    def easypost(self,endpoint:str,data:Any) ->Any:
        r"""
        简单发送post请求
        :param endpoint str 终结点 或者说是host/后面的那一部分
        :param data Any 这个是带着请求的data 可以是任何py原生对象
        :return Any 这个值一般来说是requests.Response对象 但是如果status_code不为200 那么就返回None
        """
        if endpoint[:1:] =="/":
            response=self.network("http://"+self.host+":"+str(self.port)+endpoint[1::],data=data,method="POST")
        else:
            response=self.network("http://"+self.host+":"+str(self.port)+"/"+endpoint,data=data,method="POST")
        if response.status_code!=200:
            return None
        else:
            return response.content.decode("utf-8")
    def jsonfly(self,data)-> Any:
        r"""
        自动解析json
        :param data dict/str 要转换的数据
        :return  data如果为str 那么返回dict 如果data为dict 那么返回str
        """
        typedata=type(data)
        typestr=typedata.__name__
        if typestr !="str" and typestr !="dict":
            raise cqbotapiError("data类型错误 应该为str或者dict 而不是："+str(typestr))
        else:
            if typestr=="str":
                return json.loads(data)
            else:
                return json.dumps(data)
    def send_group_msg(self,group_id:int,message:str,auto_escape=False) -> dict:
        r"""
        发送群消息
        :param group_id int 群号 或者说是群id
        :param message str 要发送的消息
        :param auto_escape bool 是否不解析cq码 默认为False
        :return message_id int 消息id
        """
        data=(self.easypost("send_group_msg",{"group_id":group_id,"message":message,"auto_escape":auto_escape}))
        if type(data).__name__ == "NoneType":
            raise cqbotapiError("go-cqhttp返回空值 请检查go-cqhttp端输出")
        else:
            return self.jsonfly()
def client(host:str,port:int) -> cqbotapi:
    return cqbotapi(host,port)