<!-- TOC -->

- [python](#python)
  - [输入文件路径，函数名称](#输入文件路径函数名称)
  - [os.path.dirname](#ospathdirname)
  - [os.path.dirname(__file__)的使用](#ospathdirnamefile的使用)
  - [模块引用](#模块引用)
    - [获取当前路径](#获取当前路径)
    - [跨目录引用](#跨目录引用)
    - [引用模块](#引用模块)
    - [搜索顺序](#搜索顺序)
    - [Python中的包](#python中的包)
    - [python2中.pyc文件](#python2中pyc文件)
    - [python3中的.pyc文件](#python3中的pyc文件)
  - [#!/usr/bin/python3](#usrbinpython3)
  - [函数传参](#函数传参)
  - [使用 python 执行管道命令](#使用-python-执行管道命令)
  - [报错处理](#报错处理)
    - [permission denied](#permission-denied)
    - [NameError: name '****' is not defined](#nameerror-name--is-not-defined)
    - [SyntaxError: Non-ASCII character '\xe7'](#syntaxerror-non-ascii-character-xe7)

<!-- /TOC -->

# python

## 输入文件路径，函数名称

```
全路径文件：__file__
文件名：   os.path.basename(__file__)
函数名:    __name__
行号：     sys._getframe().f_lineno
```

## os.path.dirname

语法：os.path.dirname(path) 
功能：去掉文件名，返回目录 
```
print(os.path.dirname('W:\Python_File\juan之购物车.py'))
#结果
#W:\Python_File
print(os.path.dirname('W:\Python_File'))
#结果
#W:\
```
## os.path.dirname(__file__)的使用

(1).当"print os.path.dirname(__file__)"所在脚本是以完整路径被运行的， 那么将输出该脚本所在的完整路径，比如：
```
python d:/pythonSrc/test/test.py
那么将输出 d:/pythonSrc/test
```
(2).当"print os.path.dirname(__file__)"所在脚本是以相对路径被运行的， 那么将输出空目录，比如：
```
python test.py
那么将输出空字符串
```

## 模块引用

每个以.py 结尾的thon 文件就是一个Python 模块(Module)。
一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。

### 获取当前路径
```
方法一：
import sys,os
os.getcwd()#然后就可以看见结果了

方法二：
import os
os.path.dirname(os.path.realpath('__file__'))#注意：添加单引号，当前python文件的上级目录
```

### 跨目录引用

python本身不支持跨目录调用文件。
将父目录（需要调用文件所在目录）加入到sys.path (python的搜索模块的路径)，之后则可以添加该目录下的任何文件了。
```
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
```

### 引用模块

python2和python3区别比较大。
查看python_import中的c.py文件，了解更多。

* import 语句

模块定义好后，我们可以使用 import 语句来引入模块，语法如下：
```
import module1[, module2[,... moduleN]]
```

* from…import 语句

Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
```
from modname import name1[, name2[, ... nameN]]
```

* from…import* 语句
```
from modname import *
```

### 搜索顺序

当你导入一个模块，Python 解析器对模块位置的搜索顺序是：

1、当前目录
2、如果不在当前目录，Python 则搜索在 shell 变量 `PYTHONPATH` 下的每个目录。
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为`/usr/local/lib/python/`。
模块搜索路径存储在 ``system` 模块的 `sys.path` 变量中。变量里包含当前目录，`PYTHONPATH`和由安装过程决定的默认目录。

### Python中的包

包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。
简单来说，包就是文件夹，但该文件夹下必须存在 `__init__.py` 文件, 该文件的内容可以为空。`__init__.py` 用于标识当前文件夹是一个包。

### python2中.pyc文件

在上述的各种自定义模块调用的操作后，如果回到之前新建的目录再多看一眼，相信不难发现，多出了几个.pyc文件，比如上面的b1.pyc、__init__.pyc，为什么会生成这些pyc文件，pyc文件又是有什么作用呢，我查阅了点资料在此说一下我的理解。
首先，来看一下python的运行和编译机制的几个步骤：
python运行自然要依赖解释器，解释器会将python源码转换为字节码，然后再执行转换好的字节码。
那么当我们在引入调用一些模块时……
模块加载的过程中，源码就被虚拟机（解释器）翻译成了PyCodeObject对象（也就是字节码）
将PyCodeObject写入了CPU，下次运行将直接从内存中进行读取指令并执行程序
执行结束后，根据执行的方式决定是否将执行的结果写回硬盘，也就是复制到.pyc文件中
当再次执行时，先检查是否有.pyc文件，有的话，再检查字节码文件与自身的修改时间是否一致，一致则直接运行.pyc文件，不一致或是没有字节码文件则从新执行前面三个 步骤。
所以，我们前面调用过的模块都有生成一个.pyc文件。
从上面的步骤进行分析，就可以看出.pyc文件相对与.py文件来说，由于是执行过并写入内存空间的，所以加载速度会比.py文件要快，可以加速程序的运行。
当然了，由于执行起来.pyc和.py是一样的，.py是直接以源码的形式进行呈现，而.pyc只是字节码文件，在某种程度上来说，还可以防止代码被偷看，具有一定的隐藏效果……

### python3中的.pyc文件

python3中的.pyc文件在__pycache__文件夹中。

pyc是编译py之后生成的本地文件。一般当我们想发布系统的时候不想让别人看到源代码，所以要提前生成pyc文件。
现今网上有很多介绍如何生成pyc的文章，但是在python3之后发现其生产pycache目录下，而不是与源文件同一目录。
那么如何让python3实现生成的pyc与源代码在同一目录呢，使用`python3 -m compileall -b .`

1. 生产pyc文件: python3 -m compileall -b .
2. 删除py文件: find . -name “*.py” |xargs rm -rf
3. 删除pycache目录: find . -name “pycache” |xargs rm -rf

## #!/usr/bin/python3

`#!/usr/bin/python3`这种写法在unix系统中表示这个脚本文件的默认启动程序，通常写在第一行，其中 `/usr/bin/python3` 是那个程序的路径(命令行输入`where python`,`where python3`可以查看`python`的安装位置)，`#` 符号在 `shell`、`python` 中均为注释的标志，将类似于 `#!/bin/bash` 的一行注释写在脚本文件的第一行，可以使脚本的使用更加方便。

`python`运行环境，如下也可以查看安装位置：
```py
import sys
print(sys.path)
```

```py
def main():
    print('hello, world!')

if __name__ == '__main__':
    main()
```
需要如下执行：
```
python3 main.py
```
如果添加了`#!/usr/bin/python3`:
```py
#!/usr/bin/python3

def main():
    print('hello, world!')

if __name__ == '__main__':
    main()
```
运行时便可以当作普通`shell`脚本那样运行(**注意**需要有运行权限)：
```
./main.py
```

## 函数传参

python3.5开始可以给参数指定类型，之前版本不能

python中函数传递参数有四种形式：

1. fun1(a,b,c)是直接将实参赋予行参，根据位置做匹配，即严格要求实参的数量与行参的数量位置相等，比较一般，大多数语言常用这种方式。
2. fun2(a=1,b=2,c=3)根据键值对的形式做实参与行参的匹配，通过这种式就可以忽略了参数的位置关系，直接根据关键字来进行赋值，同时该种传参方式还有个好处就是可以在调用函数的时候作为个别选填项，不要求数量上的相等，即可以fun5(3,4)来调用fun2函数，这里关键就是前面的3,4覆盖了原来a、b两个行参的值，但c还是不变采用原来的默认值3，这种模式相较第一种更加灵活，不仅可以通过fun6(c=5,a=2,b=7)来打乱行参的位置，而且可以在但没有对应行参传递的时候常用定义函数时的默认值。
3. fun3(*args)，这传参方式是可以传入任意个参数，这些若干参数都被放到了tuple元组中赋值给行参args，之后要在函数中使用这些行参，直接操作args这个tuple元组就可以了，这样的好处是在参数的数量上没有了限制，但是因为是tuple，其本身还是有次序的，这就仍然存在一定的束缚，在对参数操作上也会有一些不便
4. fun4(**kargs)最为灵活，其是以键值对字典的形式向函数传参，含有第二种位置的灵活的同时具有第三种方式的数量上的无限制。此外第三四种函数声明的方式前的’*’,与c里面的指针声明一样，这里仅做声明标识之用

四种传递方式混合使用，fun7(a,b,*c,**d)，但四种方式混用时要遵守：

* args = 须在args之后
* *args须在args=value之后
* **kargs须在*args之后

赋值过程为：

1. 按顺序把传给args的实参赋值给对应的行参
2. args = value 形式的实参赋值给行参
3. 将多余出的即键值对行后的零散实参打包组成一个tuple传递给*args
4. 将多余的key=value形式的实参打包正一个dicrionary传递给**kargs

## 使用 python 执行管道命令

[使用 python 执行管道命令](http://www.ccike.com/?p=118)

## 报错处理

### permission denied

没有权限，执行下面命令设置权限：
```
sudo chmod -R 777 设置权限的路径
sudo chmod -R 777 /Users/yunxi/Desktop/yunxitech/matias_github/python-story
```
* `-R` 是指级联应用到目录里的所有子目录和文件
* `777` 是所有用户都拥有最高权限

### NameError: name '****' is not defined

python函数的应用一般需要：先定义、后调用
如果函数定义在调用之后，执行将报错：
```
NameError: name '****' is not defined
```

### SyntaxError: Non-ASCII character '\xe7'

python2运行时报错：
```
SyntaxError: Non-ASCII character '\xe7' in file python_encod_decode.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```
当在Python 2.X文件中写中文注释或输出中文时候，经常会出现编译错误（在Python 3.X中没有这种错误。）这是因为Python 2.X的默认编码文件是用ASCII码

头部加上如下代码：
```
#coding=utf-8
```