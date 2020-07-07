<!-- TOC -->

- [python](#python)
    - [#!/usr/bin/python3](#usrbinpython3)
    - [函数传参](#函数传参)
    - [报错处理](#报错处理)
        - [permission denied](#permission-denied)
        - [NameError: name '****' is not defined](#nameerror-name--is-not-defined)
        - [SyntaxError: Non-ASCII character '\xe7'](#syntaxerror-non-ascii-character-\xe7)

<!-- /TOC -->

# python

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
运行时便可以当作普通`shell`脚本那样运行：
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