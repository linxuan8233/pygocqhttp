
#这个库的基本用法
=================
在httpserver.py中可以自定义触发器
-----------------
例如:
```python
from pygocqhttp import httpserver,httpapi
bot_server=httpserver.run('localhost:5700')
bot=httpapi.bot('http://localhost:5800')
@bot_server.on_message("group",group_id=123456)
def test(data):
    if data.message=="hello":
        bot.send_group_msg(group_id=data.group_id,message="world")
```
>在上面的例子中 我们定义了一个触发器 当收到123456的消息为hello时触发 并发送world  

>data是一个类 里面有很多属性 例如message group_id等 请注意的是触发的类型不同的属性也不同
例如私聊消息中没有group_id
但是相同的有 time self_id 和post_type 这三个属性是所有消息都有的
他们的含义分别是 时间戳 机器人QQ 上报类型  

>具体什么类型的消息有什么属性请看go-cqhttp的文档或者查看此文件夹下的type_info.md
go-cqhttp的文档在[这里](https://docs.go-cqhttp.org/)

>这个触发器的使用方法远不止上面的那个
例如我们可以设置在一个群里面有人@机器人时触发
```python
from pygocqhttp import httpserver,httpapi,Cqcode
bot_server=httpserver.run('localhost:5700')
bot=httpapi.bot('http://localhost:5800')
cq=Cqcode()
@bot_server.on_message("group",group_id=123456,at=1)
def test(data):
    #注意这里的消息是带at的 如果不需要带at的cq码请使用data.message_noat
    if data.message_noat=="hello":
        #这里我们还可以设置at这个人
        bot.send_group_msg(group_id=data.group_id,message=cq.at(data.user_id)+"world")
```
>在上面的例子中 我们定义了一个触发器 当收到群123456 at机器人的消息为hello时触发 并发送world 并at这个人
这里的at是一个触发器的参数 他的含义是当消息中有at机器人的时候触发

>他的值默认是布尔类型 所以也可以选择True或者False 但如果选了非0/1的数字 那就是at人的QQ号
例如
```python
from pygocqhttp import httpserver,httpapi,Cqcode
bot_server=httpserver.run('localhost:5700')
bot=httpapi.bot('http://localhost:5800')
cq=Cqcode()
@bot_server.on_message("group",group_id=123456,at=123456)
def test(data):
    #注意这里的消息是带at的 如果不需要带at的cq码请使用data.message_noat
    if data.message_noat=="hello":
        #这里我们还可以设置at这个人
        bot.send_group_msg(group_id=data.group_id,message=cq.at(data.user_id)+"world")
```
>在上面的例子中 我们定义了一个触发器 当收到群123456 at机器人的消息为hello时触发 并发送world 并at这个人
或者我们设置关键词触发

>请注意这个关键词可能是带参数的
例如
/append 123123
这里的123123就是参数
不带参数的关键词的就是长这样
/status
这里的status就是关键词 而且不带参数

>带参数的触发器是这样写的 我们还以上面的例子为例
```python
from pygocqhttp import httpserver,httpapi,Cqcode
bot_server=httpserver.run('localhost',5700)
bot=httpapi.bot('http://localhost:5800')
cq=Cqcode()
@bot_server.on_message("group",group_id=123456,at=1,keyword=("/status"),keyword_param=0)
def test(data):
    #上面的keyword_param是关键词的参数 0表示不带参数 1表示带参数 而keyword是关键词
    #调用data的args属性可以获取参数
    #此args和sys的那个args长的很像 第一个元素 就是你设置的那个关键词 如果没有参数 那么就只有这一个元素
    #如果有参数 那么就是关键词和参数
    if data.args[0]=="/status":
        bot.send_group_msg(group_id=data.group_id,message=cq.at(data.user_id)+"OK!")
```

>在上面的例子中 我们定义了一个触发器 当收到群123456 at机器人的参数为/status时触发 并发送OK! 并at这个人

>参数元组这里可以写列表 也可以设置不区分大小写 如果设置成None 那么响应全部消息
这里可以写正则 但是需要在前面加上re:
例如
re:/status\s\d+
这里的\s表示空格 \d表示数字 也就是说这个正则是匹配/status后面跟着一个空格和一个数字
如果你不知道正则的话 请自行百度

>触发器第一个的参数"group"表示群消息 这里可以写列表 即响应不同的类型的消息 但是请注意不用类型的消息有不同的属性 请做好判断

>可以写的类型有
    * group 群消息
    * private 私聊消息
    * notice 撤回消息
    * friend_recall 好友撤回消息
    * group_recall  群撤回消息
    * group_upload 群文件上传
    * group_admin 群管理员变动
    * group_decrease 群成员减少
    * group_increase 群成员增加
    * group_ban 群禁言
    * friend_add 好友添加
    * group_name 群名变更
    * group_card 群名片变更
    * group_leave 群成员离开
    * group_special_title 群成员群头衔变更
    * group_poke 群成员戳一戳
    * group_honor 群成员荣誉变更
    * friend_poke 好友戳一戳
    * client_status 客户端状态变更
    * essence q群精华消息

>下面是特殊的类型
    * heartbeat	心跳
    * ** 所有事件

>这里的**表示所有事件 也就是说这个触发器会响应所有的事件 但是我们不建议这样写 因为这样写了会导致你程序很卡
如果你想要响应所有事件 可以看看下面的例子
```python
from pygocqhttp import httpserver,httpapi,Cqcode
bot_server=httpserver.run('localhost',5700)
bot=httpapi.bot('http://localhost:5800')
cq=Cqcode()
@bot_server.on_message("**")
def test(data):
    #这时候就是全部类型了 你需要用if来判断
    #调用data.type去判断类型
    if data.type=="group":
        #这里就是群消息了
        bot.send_group_msg(group_id=data.group_id,message=cq.at(data.user_id)+"OK!")
    #又或者是群里有个人戳了一下bot
    elif data.type=="group_poke":
        bot.send_group_msg(group_id=data.group_id,message=cq.at(data.user_id)+"别戳我")
    #总之这样写会很卡
```

>触发器的全部教程可以去看[httpserverhelp.md](./httpserverhelp.md)

>现在我们来说说如何使用httpapi
```python
from pygocqhttp import httpapi
#创建一个bot对象
#注意这里的地址是go-cqhttp的httpapi地址 如果不会配置请去查看go-cqhttp的配置文件
bot=httpapi.bot('http://localhost:5800')
#发送群消息
bot.send_group_msg(group_id=123456,message="hello")
#上面的123456是群号 message是消息
#发送私聊消息
bot.send_private_msg(user_id=123456,message="hello")
#上面的123456是qq号 message是消息
#或者其他的api
```
<h6>有一说一这玩意有够简单的</h6>

>这下面是Cqcode的教程
这个模块主要是封装了CQ码
比如说图片 at 戳一戳 语音等等
使用方法也很简单
```python
from pygocqhttp import Cqcode
#创建一个Cqcode对象
cq=Cqcode()
#先at人
at=cq.at(123456)#这里写的是qq号
#然后调用httpapi的send_group_msg方法即可at人
#同样发图片和语音也是一样的
```
<h6>有一说一这是我第一次用markdown</h6>