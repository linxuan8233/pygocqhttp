"""
入口文件
适配于go-cqhttp
简单封装了下列方法
cq码类
httpapi类
还有触发器等
这个库基于go-cqhttp的http通讯 而不是websocket
如果你想使用websocket请使用nonebot 那个写的比我完善
"""
from .httpapi import *
__version__ = "1.0.0"
