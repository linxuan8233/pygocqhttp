r"""
CqCode模块
Lx c2022
Linxuan@lxdn.cc
"""

from .Error import *
class cqon:
    r"""Python字典与Cq码字符串互转"""
    def __init__(self) -> None:
        pass
    def load(self,cqcode:str) ->dict:
        r"""
        把cq码转换为Python字典
        :param cqcode str cq码字符串
        :return pydict dict Python的字典类型
        """
        if cqcode:
            try:
                cqargv=cqcode.split("[")[1].split("]")[0].split(",")
                if len(cqargv)<1:
                    raise CqError("该值似乎不是cq码")
                else:
                    py_dict={}
                    for argc in cqargv[1::]:
                        key,val=argc.split("=")
                        py_dict[key]=val
                    return (cqargv[0].split(":")[1],py_dict)
            except Exception:
                raise CqError("该值似乎不是cq码")
        else:
            return {}
    def dump(self,type1:str,pydict:dict) -> str:
        r"""
        把Python中的字典转化为cq码字符串
        :param type1 str cq码类型
        :param pydict dict python的字典类型
        :return cqcode str 返回cq码字符串
        """
        if pydict:
            if type(pydict).__name__=='dict':
                cqhead="[CQ:"+str(type1)+",%s]"
                cqarvc=""
                pydictkey=list(pydict.keys())
                for i in range(len(pydictkey)):
                    if i==len(pydictkey)-1:
                        cqarvc+=pydictkey[i]+"="+str(pydict[pydictkey[i]])
                    else:
                        cqarvc+=pydictkey[i]+"="+str(pydict[pydictkey[i]])+","
                return cqhead %(cqarvc.strip())
            else:
                raise CqError("该数据似乎不是Python中的字典")
        else:
            raise CqError("值为空")
class cqcode():
    r"""cq码函数 
    参考https://docs.go-cqhttp.org/cqcode/
    """
    def __init__(self) -> None:
        self.cq=cqon()
    def at(self,qq:int) ->str:
        r"""
        @某人
        :param qq int 要@的人的QQ号
        """
        if type(qq).__name__ == "int" or type(qq).__name__ == "str":
            return self.cq.dump(type1="at",pydict={"qq":qq})
        else:
            raise CqError("qq只能为int 或者str")
    def face(self,qid:int) ->str:
        r"""
        发送表情（黄脸）的cq码 id表见此https://github.com/kyubotics/coolq-http-api/wiki/%E8%A1%A8%E6%83%85-CQ-%E7%A0%81-ID-%E8%A1%A8
        :param qid int 表情id
        """
        if type(qid).__name__ =="int" or type(qid).__name__=="str":
            return self.cq.dump("face",{"id":qid})
        else:
            raise CqError("表情id只能为int 或者str")
    def record(self,file:str,magic:int=0,cache:int=1,proxy:int=0,timeout:int=0) ->str:
        r"""
        发送语音
        :param file str 文件名
        :parammagic 0/1 默认 0, 设置为 1 表示变声
        :param magic 0/1 默认 0, 设置为 1 表示变声
        :param cache 0/1 只在通过网络 URL 发送时有效, 表示是否使用已缓存的文件, 默认 1
        :param proxy 0/1 只在通过网络 URL 发送时有效, 表示是否通过代理下载文件 ( 需通过环境变量或配置文件配置代理 ) , 默认 0
        :param timeout int 只在通过网络 URL 发送时有效, 单位秒, 表示下载网络文件的超时时间 , 默认不超时
        :return cqcode str 返回对应的cq码字符串
        """
        if timeout:
            return self.cq.dump("record",{"file":file,"magic":magic,"cache":cache,"proxy":proxy,"timeout":timeout})
        else:
            return self.cq.dump("record",{"file":file,"magic":magic,"cache":cache,"proxy":proxy})
    def poke(self,qq:int) ->str:
        r"""
        戳一下某个人
        :param qq int 要戳的人的QQ号
        """
        if type(qq).__name__ == "int" or type(qq).__name__ == "str":
            return self.cq.dump(type1="poke",pydict={"qq":qq})
        else:
            raise ValueError("qq只能为int 或者str")
    def image(self,file=None,url=None,cache=1,id=40000,c=2,type=None,subType=None)->str:
        r"""
        发送图片
        :param file str 文件名
        :param url str 网络图片链接
        :param cache 0/1 只在通过网络 URL 发送时有效, 表示是否使用已缓存的文件, 默认 1
        :param id int 只在通过网络 URL 发送时有效, 表示图片类型, 默认 40000
        :param c int 只在通过网络 URL 发送时有效, 表示图片类型, 默认 2
        :param type str 只在通过网络 URL 发送时有效, 表示图片类型, 默认 None
        :param subType str 只在通过网络 URL 发送时有效, 表示图片类型, 默认 None
        """
        if file and url:
            raise CqError("请选择一个图片值传入")
        else:
            if url:
                return self.cq.dump("image",{"url":url, "cache":cache, "id":id, "type":type, "subType":subType})
            elif file:
                return self.cq.dump("image",{"file":file,"cache":cache, "id":id, "type":type, "subType":subType})
            else:
                raise CqError("File或者url只能二选一")
    def share(self,url:str,title:str,content:str,image:str=None) ->str:
        r"""
        发链接
        """
        if image:
            return self.cq.dump("share",{"url":url,"title":title,"content":content,"image":image})
        else:
            return self.cq.dump("share",{"url":url,"title":title,"content":content})
    def music(self,type:str,id:int) ->str:
        r"""
        发送音乐
        :param type str 可能的值：163/qq/xm
        :param id int 音乐id
        """
        return self.cq.dump("music",{"type":type,"id":id})
    def diy_music(self,type:str,url:str,audio:str,title:str,content:str=None,image:str=None) ->str:
        r"""
        发送自定义音乐卡片
        :param type str 可能的值：custom
        :param url str 点击后跳转的地址
        :param title str 标题
        :param content str 歌曲简介可选
        :param image str 封面图片链接可选
        """
        if content and image:
            return self.cq.dump("music",{"type":type,"url":url,"audio":audio,"title":title,"content":content,"image":image})
        elif content:
            return self.cq.dump("music",{"type":type,"url":url,"audio":audio,"title":title,"content":content})
        elif image:
            return self.cq.dump("music",{"type":type,"url":url,"audio":audio,"title":title,"image":image})
        else:
            ...
    def reply(self,id:int,text:str,qq:int=None,time:int=None,seq:int=None)->str:
        r"""
        回复消息
        :param id int 消息id
        :param text str 回复的内容
        :param qq int 可选, 回复的对象的QQ号
        :param time int 可选, 回复的对象的时间戳
        :param seq int 可选, 回复的对象的消息序号
        """
        if qq and time and seq:
            return self.cq.dump("reply",{"id":id,"text":text,"qq":qq,"time":time,"seq":seq})
        elif qq and time:
            return self.cq.dump("reply",{"id":id,"text":text,"qq":qq,"time":time})
        elif qq:
            return self.cq.dump("reply",{"id":id,"text":text,"qq":qq})
        else:
            return self.cq.dump("reply",{"id":id,"text":text})
    def gift(self,qq:int,gift:int) ->str:
        r"""
        发送礼物
        :param qq int 对方QQ号
        :param gift int 礼物id
        关于这个礼物id 只能发送下列这些
        ID    名称
        0	甜 Wink
        1	快乐肥宅水
        2	幸运手链
        3	卡布奇诺
        4	猫咪手表
        5	绒绒手套
        6	彩虹糖果
        7	坚强
        8	告白话筒
        9	牵你的手
        10	可爱猫咪
        11	神秘面具
        12	我超忙的
        13	爱心口罩
        """
        return self.cq.dump("gift",{"qq":qq,"id":gift})
    def node(self,id:int,name:str,uin:int,content:str,seq:str) ->str:
        r"""
        合并转发消息节点
        :param id int 消息id
        :param name str 发送者昵称
        :param uin int 发送者QQ号
        :param content str 消息内容
        :param seq str 具体消息
        *需要用特殊函数发送：httpapi.send_group_forward_msg 且只支持元组的形式传入消息
        """
        return self.cq.dump("node",{"id":id,"name":name,"uin":uin,"content":content,"seq":seq})