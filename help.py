#此py文件写这个库的一些方法

#先说一下这里面几个py文件的作用
#Cqcode.py是cq码的处理
#httpapi.py是httpapi的接口
#help.py是一些帮助
#__init__.py是入口
#Error.py是错误类
#cqhttpytype.py是自定义的一些类型

#在httpserver.py中可以自定义触发器
#例如
"""
from pygocqhttp import httpserver,httpapi
bot_server=httpserver.run('localhost',5700)
bot=httpapi.bot('http://localhost:5800')
@bot_server.on_message("group",group_id=123456)
def test(data):
    if data.message=="hello":
        bot.send_group_msg(group_id=data.group_id,message="world")
"""
#在上面的例子中 我们定义了一个触发器 当收到群123456的消息为hello时触发 并发送world
#data是一个类 里面有很多属性 例如message group_id等 请注意的是触发的类型不同的属性也不同
#例如私聊消息中没有group_id
#但是相同的有 time self_id 和post_type 这三个属性是所有消息都有的
#他们的含义分别是 时间戳 机器人QQ 上报类型
#具体什么类型的消息有什么属性请看go-cqhttp的文档或者查看此文件夹下的type_info.py
#go-cqhttp的文档在这里 https://docs.go-cqhttp.org/
#这个触发器的使用方法远不止上面的那个
#例如
#我们可以设置在一个群里面有人@机器人时触发
"""
from pygocqhttp import httpserver,httpapi,Cqcode
bot_server=httpserver.run('localhost',5700)
bot=httpapi.bot('http://localhost:5800')
cq=Cqcode()
@bot_server.on_message("group",group_id=123456,at=1)
def test(data):
    #注意这里的消息是带at的 如果不需要at的cq码请使用data.message_noat
    if data.message_noat=="hello":
        #这里我们还可以设置at这个人
        bot.send_group_msg(group_id=data.group_id,message=cq.at(data.user_id)+"world")
"""
#在上面的例子中 我们定义了一个触发器 当收到群123456 at机器人的消息为hello时触发 并发送world 并at这个人
#这里的at是一个触发器的参数 他的含义是当消息中有at机器人的时候触发
#他的值默认是布尔类型 所以也可以选择True或者False 但如果选了非0/1的数字 那就是at人的QQ号
#例如
"""
from pygocqhttp import httpserver,httpapi,Cqcode
bot_server=httpserver.run('localhost',5700)
bot=httpapi.bot('http://localhost:5800')
cq=Cqcode()
@bot_server.on_message("group",group_id=123456,at=123456)
def test(data):
    #注意这里的消息是带at的 如果不需要at的cq码请使用data.message_noat
    if data.message_noat=="hello":
        #这里我们还可以设置at这个人
        bot.send_group_msg(group_id=data.group_id,message=cq.at(data.user_id)+"world")
"""
#在上面的例子中 我们定义了一个触发器 当收到群123456 at机器人的消息为hello时触发 并发送world 并at这个人
#或者我们设置关键词触发
#请注意这个关键词可能是带参数的
#例如
#/append 123123
#这里的123123就是参数
#不带参数的关键词的就是长这样
#/status
#这里的status就是关键词 而且不带参数
#带参数的触发器是这样写的 我们还以上面的例子为例
"""
from pygocqhttp import httpserver,httpapi,Cqcode
bot_server=httpserver.run('localhost',5700)
bot=httpapi.bot('http://localhost:5800')
cq=Cqcode()
"""