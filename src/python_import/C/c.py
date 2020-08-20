#!/usr/bin/python3
#coding=utf-8

import sys,os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上级目录
# sys.path.append(BASE_DIR)
# print(BASE_DIR)

sys.path.append('..')# python2 可以使用相对路径，python3中使用上面的方法

import cc #同级目录下引用文件

# from D import d # 同级目录下的目录下文件引用
# from D.d import *
import D.d

# python3 中上面三种都是可以的
# python2 中包需要__init__.py文件（文件可以为空）才能运行成功

# from ..a import a_debug
# 相对引用会报错
# ValueError: attempted relative import beyond top-level package
from a import a_debug

# from ..B import b
# 相对引用会报错
# ValueError: attempted relative import beyond top-level package
from B import b
from B.b import b_debug
# python3 中是可以的
# python2 中包需要__init__.py文件（文件可以为空）才能运行成功

cc.cc_debug()

# d.d_debug()
# d_debug()
# d_one()
# d_two()

D.d.d_debug()
D.d.d_one()
D.d.d_two()

b.b_debug()
a_debug()
b.b_debug()
b_debug()

if __name__ == "__main__":
    print('main')