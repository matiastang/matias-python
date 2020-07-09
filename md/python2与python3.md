<!-- TOC -->

- [python2与python3](#python2与python3)
    - [typing模块的作用](#typing模块的作用)
    - [SyntaxError: Non-ASCII character '\xe7'](#syntaxerror-non-ascii-character-\xe7)
    - [TypeError: a bytes-like object is required, not 'str'](#typeerror-a-bytes-like-object-is-required-not-str)

<!-- /TOC -->

# python2与python3

## typing模块的作用

[官网typing详细说明](https://docs.python.org/zh-cn/3/library/typing.html#module-typing)

自python3.5开始，PEP484为python引入了类型注解(type hints)

* 类型检查，防止运行时出现参数和返回值类型、变量类型不符合。
* 作为开发文档附加说明，方便使用者调用时传入和返回参数类型。
* 该模块加入后并不会影响程序的运行，不会报正式的错误，只有提醒pycharm目前支持typing检查，参数类型错误会黄色提示

## SyntaxError: Non-ASCII character '\xe7'

python2运行时报错：
```
SyntaxError: Non-ASCII character '\xe7' in file python_encod_decode.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```
当在Python 2.X文件中写中文注释或输出中文时候，经常会出现编译错误（在Python 3.X中没有这种错误。）这是因为Python 2.X的默认编码文件是用ASCII码

头部加上如下代码：
```
#coding=utf-8
```

## TypeError: a bytes-like object is required, not 'str'

python3和Python2在套接字返回值解码上有区别。

解决办法非常的简单，只需要用上python的bytes和str两种类型转换的函数encode()、decode()即可！

str通过encode()方法可以编码为指定的bytes；
反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法；
```
str = 'this is fujieace.com test'
os.write(fd,bytes(str,'UTF-8'))
```