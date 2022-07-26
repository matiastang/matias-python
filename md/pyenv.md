<!--
 * @Author: matiastang
 * @Date: 2022-07-26 15:35:46
 * @LastEditors: matiastang
 * @LastEditTime: 2022-07-26 17:38:56
 * @FilePath: /matias-python/md/pyenv.md
 * @Description: pyenv
-->
# pyenv

[python版本下载地址](https://www.python.org/downloads/source/)
[pyenv的github地址](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fpyenv%2Fpyenv)
[pyenv-vitualenv插件地址](https://link.zhihu.com/?target=https%3A//github.com/pyenv/pyenv-virtualenv.git)
[pyenv安装](https://zhuanlan.zhihu.com/p/36402791/)

`pyenv`是管理`python`版本的工具。安装`pyenv`后，可以管理各种`python`版本，并且各个版本的环境完全独立，互不干扰。

`pyenv`是一个`forked`自`ruby`社区的简单、低调、遵循`UNIX`哲学的`Python`环境管理工具, 它可以轻松切换全局解释器版本, 同时结合`vitualenv`插件可以方便的管理对应的包源。

## 安装

pyenv已经在github上开源，我们直接从github上clone项目到本地

```
$ pyenv version
zsh: command not found: pyenv
```
```
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
Cloning into '/Users/matias/.pyenv'...
remote: Enumerating objects: 21745, done.
remote: Counting objects: 100% (503/503), done.
remote: Compressing objects: 100% (151/151), done.
remote: Total 21745 (delta 369), reused 439 (delta 334), pack-reused 21242
Receiving objects: 100% (21745/21745), 4.37 MiB | 57.00 KiB/s, done.
Resolving deltas: 100% (14709/14709), done.
```
* MacOS的话可以直接用`homebrew`安装
```
$ brew update
$ brew install pyenv
```
添加shell配置文件中追加如下: (如zshrc)
```
export PYENV_ROOR="$HOME/.pyenv"
export PATH=$PYENV_ROOT/shims:$PATH
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
* `.profile`
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init --path)"' >> ~/.profile
```
* `.zprofile`
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
```
```
$ source ~/.zprofile
```
```
$ pyenv version
system (set by /Users/matias/.pyenv/version)
```
* 查看可安装的版本
```
$ pyenv install -l
Available versions:
  2.1.3
  2.2.3
  2.3.7
  2.4.0
  2.4.1
  2.4.2
  2.4.3
  2.4.4
  2.4.5
  2.4.6
  2.5.0
  2.5.1
  2.5.2
  2.5.3
  2.5.4
  2.5.5
  2.5.6
  2.6.0
  2.6.1
  2.6.2
  2.6.3
  2.6.4
  2.6.5
  2.6.6
  2.6.7
  2.6.8
  2.6.9
  2.7.0
  2.7-dev
  2.7.1
  2.7.2
  2.7.3
  2.7.4
  2.7.5
  2.7.6
  2.7.7
  2.7.8
  2.7.9
  2.7.10
  2.7.11
  2.7.12
  2.7.13
  2.7.14
  2.7.15
  2.7.16
  2.7.17
  2.7.18
  3.0.1
  3.1.0
  3.1.1
  3.1.2
  3.1.3
  3.1.4
  3.1.5
  3.2.0
  3.2.1
  3.2.2
  3.2.3
  3.2.4
  3.2.5
  3.2.6
  3.3.0
  3.3.1
  3.3.2
  3.3.3
  3.3.4
  3.3.5
  3.3.6
  3.3.7
  3.4.0
  3.4-dev
  3.4.1
  3.4.2
  3.4.3
  3.4.4
  3.4.5
  3.4.6
  3.4.7
  3.4.8
  3.4.9
  3.4.10
  3.5.0
  3.5-dev
  3.5.1
  3.5.2
  3.5.3
  3.5.4
  3.5.5
  3.5.6
  3.5.7
  3.5.8
  3.5.9
  3.5.10
  3.6.0
  3.6-dev
  3.6.1
  3.6.2
  3.6.3
  3.6.4
  3.6.5
  3.6.6
  3.6.7
  3.6.8
  3.6.9
  3.6.10
  3.6.11
  3.6.12
  3.6.13
  3.6.14
  3.6.15
  3.7.0
  3.7-dev
  3.7.1
  3.7.2
  3.7.3
  3.7.4
  3.7.5
  3.7.6
  3.7.7
  3.7.8
  3.7.9
  3.7.10
  3.7.11
  3.7.12
  3.7.13
  3.8.0
  3.8-dev
  3.8.1
  3.8.2
  3.8.3
  3.8.4
  3.8.5
  3.8.6
  3.8.7
  3.8.8
  3.8.9
  3.8.10
  3.8.11
  3.8.12
  3.8.13
  3.9.0
  3.9-dev
  3.9.1
  3.9.2
  3.9.4
  3.9.5
  3.9.6
  3.9.7
  3.9.8
  3.9.9
  3.9.10
  3.9.11
  3.9.12
  3.9.13
  3.10.0
  3.10-dev
  3.10.1
  3.10.2
  3.10.3
  3.10.4
  3.10.5
  3.11.0b4
  3.11-dev
  3.12-dev
```
* 安装新的`Python`版本
```
$ pyenv install 3.10.5
```
* 查看所有版本
```
$ pyenv versions
```
* 使用某个版本
```
$ pyenv global 3.6.12
```
* 查看是否切换成功
```
$ python --version
```
## 使用

* 查看当前版本
pyenv version

* 查看所有版本
pyenv versions

* 查看所有可安装的版本
pyenv install --list

* 安装指定版本
pyenv install 3.6.5
* 安装新版本后rehash一下
pyenv rehash

* 删除指定版本
pyenv uninstall 3.5.2

* 指定全局版本
pyenv global 3.6.5

* 指定多个全局版本, 3版本优先
pyenv global 3.6.5 2.7.14

* 实际上当你切换版本后, 相应的pip和包仓库都是会自动切换过去的

pyenv commands：查看所有pyenv命令
pyenv exec：使用特定Python版本执行某条命令
pyenv global：设置或查看全局Python版本
pyenv hooks：列出给出的pyenv命令的钩子脚本
pyenv init：配置shell环境
pyenv install：安装某个版本的Python
pyenv local：为某个应用设置特定的Python版本
pyenv prefix：显示对应Python版本的路径前缀
pyenv rehash：再哈希pyenv shims（不清楚有什么用，欢迎评论补充）
pyenv root：显示pyenv根目录
pyenv shell：为某个shell设置特定的Python版本（与pyenv local类似）
pyenv shims：列出当前存在的shims（pyenv的工作原理就是在一个叫shims的目录下创建Python解释器的“假版本”，寻找Python应用时先从该目录查找）
pyenv uninstall：卸载某个版本Python
pyenv --version：显示pyenv版本
pyenv version：显示当前Python版本，等价于pyenv version-name+pyenv version-file
pyenv version-file/version-name/version-origin：当前Python版本对应的文件/名字/位置
pyenv whence：列出已安装的一个范围内的Python版本，比如列出本地安装的Python2到Python3的版本，可以使用pyenv whence 2to3
pyenv which：列出可执行文件的绝对路径，比如pyenv which python可以列出python命令的绝对路径

## pyenv安装python慢

[pyenv安装python慢](https://www.freesion.com/article/12701042365/)

使用 pyenv 安装 python 时，默认从 python.org 下载指定版本，往往特别慢，经常下载失败，这时可以先从官网下载所需要的版本的源代码到 ~/.pyenv/cache 目录下，再执行安装命令（亲测很好用）。

注意这里要下载的是类似于 Python-3.7.3.tar.xz 这样的压缩文件，要到官网 [sourcecode](https://www.python.org/downloads/source/) 页面 才可以下载。

如果是下载 `python` 源码这一步慢，那么可以参考我的办法。
`mkdir $PYENV_ROOT/cache` 然后用别的方法下载 `Python` 源码放到该目录下。
这个路径是由 `PYTHON_BUILD_CACHE_PATH` 控制的，默认值是 `"$PYENV_ROOT/cache"`，但是文件夹并不是默认创建的。
相关代码可以自己查看 https://github.com/pyenv/pyenv/blob/master/plugins/python-build/bin/pyenv-install#L183

由于pyenv install xxx下载速度十分缓慢，甚至经常被墙。。找到一个解决方案并记录下来

使用国内源

#3.7.5是版本号， -P是下载到指定目录，如果没用cache目录必须先创建此目录
wget http://mirrors.sohu.com/python/3.7.5/Python-3.7.5.tar.xz -P ~/.pyenv/cache/
 
#如果有想下载其他，那么把版本号改掉即可，格式如下 $v 代表版本
wget http://mirrors.sohu.com/python/$v/Python-$v.tar.xz -P ~/.pyenv/cache/
下载完成以后运行命令即可

**注意**wget的方式未成功下载，好像是因为mirrors.sohu.com下面没有python的目录了

[查看python的版本](https://mirrors.sohu.com/)
[镜像](http://mirrors.ustc.edu.cn/)

pyenv install 3.7.5



## pyenv和流行的pipenv、virtualenv的关系

* pipenv是requests 作者 Kenneth Reitz大神写的一个python虚拟环境管理工具, 结合了pip和virtualenv的功能, 侧重点还是在包环境管理上, 使用思路是先创建一个指定python版本的环境, 然后在此环境上安装相应的包, 好评不错, 看到很多大牛都在推荐.

* virtualenv是一个比较传统成熟的虚拟环境管理工具了, 用的人也比较多, 思路也是创建虚拟环境, 然后安装相应的包, 要进入环境就source一下activate脚本激活一下, 尽管成熟, 但是我个人不太喜欢用, 在部署项目的时候老是容易出现一些环境问题.

* pyenv相对来说知名度就差很多了, 不过也很稳定, 这三个环境管理工具我都用过, 我个人更喜欢pyenv, 理由如下:

1. 相对于其他两个工具, pyenv更侧重在python 解释器版本管理上, 比包管理更大一个层级, 使用pyenv我可以方便的下载指定版本的python解释器, pypy, anaconda等, 可以随时自由的在shell环境中本地、全局切换python解释器
2. 开发的时候不需要限定某个版本的虚拟环境, 只需要在部署的时候用pyenv指定某个版本就好了
3. pyenv切换解释器版本的时候, pip和ipython以及对应的包环境都是一起切换的, 所以如果你要同时运行ipython2.x和ipython3.x多个解释器验证一些代码时就很方便
4. pyenv也可以创建好指定的虚拟环境, 但不需要指定具体目录, 自由度更高, 使用也简单

## 包管理插件pyenv-virtualenv

首先下载:

$ git clone https://github.com/pyenv/pyenv-virtualenv.git $.pyenv/plugins/pyenv-virtualenv
克隆完成后添加如下到shell配置文件(mac的话是.zshrc)

$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
实际上mac用户直接brew安装就可以了...

$ brew install pyenv-virtualenv
$ eval "$(pyenv init -)"
$ eval "$(pyenv virtualenv-init -)"
使用:

# 创建一个3.6.5版本的虚拟环境, 命名为v365env, 然后激活虚拟环境
$ pyenv virtualenv 3.6.5 v365env
$ pyenv activate v365env
# 关闭虚拟环境
$ pyenv deactivate v365env
当切换python解释器的时候对应的pip和包库也会一并切换过去, 而且可以为指定版本的解释器创建项目所需的虚拟环境, 切换的时候也异常简单, 个人常用的做法是为每个项目创建不同的虚拟环境, 当进入该环境的时候就可以随便浪而不用担心影响到其它项目, 搭配Pycharm使用效果更佳.