<!--
 * @Author: your name
 * @Date: 2021-09-17 10:35:04
 * @LastEditTime: 2021-09-17 11:19:20
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /matias-python/md/python多版本管理.md
-->
# python多版本管理

1. 
使用brew安装pyenv
安装pyenv下的Anaconda

2. 
pyenv-virtualenv的虚拟环境

3.  
[pipenv](https://github.com/kennethreitz/pipenv)

Pipfile 与 Pipfile.lock 是社区拟定的依赖管理文件，用于替代过于简陋的 requirements.txt 文件. 过去大家经常使用virtualenv来创建虚拟环境，通过pip freeze生成requirements.txt文件，然后通过pip install -r requirements.txt进行项目模块的管理与安装。这样的安装存在很多问题，比如每次更新模块后，需要手动的重新生成依赖文件，等等问题

pipx install pipenv

### pyenv

pyenv是管理python版本的工具。安装pyenv后，可以管理各种python版本，并且各个版本的环境完全独立，互不干扰
[pyenv的github地址](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fpyenv%2Fpyenv)

### 安装pipx

[pipx](https://pypi.org/project/pipx/)

pipx 是一种帮助您安装和运行用 Python 编写的最终用户应用程序的工具。它大致类似于 macOS 的brew、JavaScript 的`npx`和 Linux 的apt.

它与 pip 密切相关。事实上，它使用 pip，但专注于安装和管理可以直接作为应用程序从命令行运行的 Python 包。

## pip和pip3的安装

pip 是一个 Python 包也是 Python 推荐的包管理程序，可以用于安装和管理 Python 包，Python 2.7.9+ 版本中已经自带了 pip 包。针对 Python 2 和 3，pip 分别提供了 pip 和 pip3 两个命令

### 安装pip

sudo easy_install pip

这个会默认安装pip2

pip是python的包管理工具，在Python2.7的安装包中，easy_install.py是默认安装的，而pip需要我们手动安装。
打开终端：

sudo easy_install pip

查看版本

pip --version

安装和更新pip

pip install --upgrade pip

### pip3

在python3的路径下
curl https://bootstrap.pypa.io/get-pip.py | python3

查看相应的包

pip3 list

安装和更新pip

pip install --upgrade pip

**注意**

小知识:
    使用easy_install或pip安装Python第三方库时,默认源地址是:https://pypi.python.org/simple/ 
这是这个源有几个问题:
    1.国外的网站访问速度比较慢.
    2.使用该源遵循http协议,若机器上没有安装openssl或ssl配置不对,将导致easy_install或pip访问该源            
    失败,若想解决这两个问题，
     可以使用国内的PyPI镜像源(会定期的把国外的软件拷贝到这个库中)。
    国内的一些pipy的镜像源:
        1.清华源:  https://pypi.tuna.tsinghua.edu.cn/simple
        2.豆瓣源:  https://pypi.douban.com/simple
        3.pypi.hustunique.com
 
 
访问国内的pipy源时,安装命令为:
      pip install 库名==1.11.11 -i https://pypi.tuna.tsinghua.edu.cn/simple