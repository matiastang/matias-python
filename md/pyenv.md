<!--
 * @Author: matiastang
 * @Date: 2022-07-26 15:35:46
 * @LastEditors: matiastang
 * @LastEditTime: 2022-07-26 15:59:20
 * @FilePath: /matias-python/md/pyenv.md
 * @Description: pyenv
-->
# pyenv

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