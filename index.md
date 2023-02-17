#这是什么？
---
这是一个基于go-cqhttp的python封装模块，用于快速开发QQ机器人。
用法类似于flask 比如你可以这样写一个机器人
```python
from pygocqhttp import httpserver,httpapi,Cqcode
bot_server=httpserver.run('localhost:5700')
bot=httpapi.bot('http://localhost:5800')
cq=Cqcode()
@bot_server.on_message("group",group_id=123456,at=1)
def test(data):
    if data.message_noat=="hello":
        bot.send_group_msg(group_id=data.group_id,message=cq.at(data.user_id)+"world")
```
这就是这个库的基本用法
---
#安装
如果你是windows用户 那么只需要进入cmd或者powershell输入
```batch
pip install -r requirements.txt
```
然后把这个库放到你的项目文件夹中 并导入即可

如果你是linux用户 那么你需要安装python3.8+和pip3
然后进入终端输入
```bash
pip3 install -r requirements.txt
```
然后把这个库放到你的项目文件夹中 并导入即可
---
>如果你遇到什么问题 那么请发issue
如果遇到bug之类的 请给我发邮件或者加我QQ
我的邮箱:[linxuan@lxdn.cc](mailto:linxuan@lxdn.cc)
我的qq是:3455576401
大佬们给个star吧
---
#具体请看[help.md](./help.md)