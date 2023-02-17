#这是什么玩意？
---
>这是一个基于go-cqhttp的python封装，用于快速开发qq机器人
    可以很轻松的创建一个你自己的qq机器人

#用法：
```python
from pygocqhttp import httpserver,httpapi,Cqcode
bot_server=httpserver.new('localhost',5700)
bot=httpapi.bot('http://localhost:5800')
cq=Cqcode()
@bot_server.on_message("group")
def test(data):
    bot.send_group_msg(group_id=data.group_id,message=cq.at(data.user_id)+"OK!")
bot.run()
```
详细帮助请看[help.md](./help.md)

#安装：
    windows:
    ```batch
        pip install -r requirements.txt
    ```
    linux:
    ```bash
        pip3 install -r requirements.txt
    ```
#联系我：
    邮箱：[linxuan@lxdn.cc](mailto:linxuan@lxdn.cc)
    QQ:3455576401
<h6>PS:这玩意应该是我搓出来的第一个项目 求各位大佬给个star罢（</h6>