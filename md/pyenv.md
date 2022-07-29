<!--
 * @Author: matiastang
 * @Date: 2022-07-26 15:35:46
 * @LastEditors: matiastang
 * @LastEditTime: 2022-07-29 16:23:46
 * @FilePath: /matias-python/md/pyenv.md
 * @Description: pyenv
-->
# pyenv

[pip,pipenv,pyenv](https://cdn.modb.pro/db/29564)

[Github-pyenv-installer](https://github.com/pyenv/pyenv-installer)
[python版本下载地址](https://www.python.org/downloads/source/)
[pyenv的github地址](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fpyenv%2Fpyenv)
[pyenv-vitualenv插件地址](https://link.zhihu.com/?target=https%3A//github.com/pyenv/pyenv-virtualenv.git)
[pyenv安装](https://zhuanlan.zhihu.com/p/36402791/)
[pyenv比 pythonbrew 和 pythonz 好在哪里？](https://github.com/pyenv/pyenv/wiki/Why-pyenv%3F)
[pyenv 官方安装](https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv)

`pyenv`是管理`python`版本的工具。安装`pyenv`后，可以管理各种`python`版本，并且各个版本的环境完全独立，互不干扰。

`pyenv`是一个`forked`自`ruby`社区的简单、低调、遵循`UNIX`哲学的`Python`环境管理工具, 它可以轻松切换全局解释器版本, 同时结合`vitualenv`插件可以方便的管理对应的包源。

## 安装

**注意**如果要通过共享库的方式安装Python，可使用如下命令：
```
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.5.2
```
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
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
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
对于Zsh：
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```
如果您还希望在非交互式登录 shell 中获取 Pyenv，还可以将命令添加到~/.zprofileor ~/.zlogin。
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
* 安装新的`Python`版本,[遇到编译失败，可以参考官方提供的解决方案 Common-build-problems](https://github.com/pyenv/pyenv/wiki/Common-build-problems)
```
$ pyenv install 3.10.5

查看信息
$ pyenv install -v 3.10.5
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

## 错误

### 安装新的`Python`版本`pyenv install 3.10.5`或`pyenv install -v 3.10.5`报错

[#1245](https://github.com/pyenv/pyenv/issues/1245)

```
ld: warning: ld: warning: directory not found for option '-L/Users/matias/.pyenv/versions/3.10.5/lib'directory not found for option '-L/Users/matias/.pyenv/versions/3.10.5/lib'

ld: warning: directory not found for option '-L/Users/matias/.pyenv/versions/3.10.5/lib'
ld: warning: directory not found for option '-L/Users/matias/.pyenv/versions/3.10.5/lib'
Undefined symbols for architecture x86_64:
  "_libintl_bindtextdomain", referenced from:
Undefined symbols for architecture x86_64:
  "_libintl_bindtextdomain", referenced from:
      __locale_bindtextdomain in libpython3.10.a(_localemodule.o)
      __locale_bindtextdomain in libpython3.10.a(_localemodule.o)
  "_libintl_dcgettext", referenced from:
  "_libintl_dcgettext", referenced from:
      __locale_dcgettext in libpython3.10.a(_localemodule.o)
  "_libintl_dgettext", referenced from:
      __locale_dcgettext in libpython3.10.a(_localemodule.o)
      __locale_dgettext in libpython3.10.a(_localemodule.o)
  "_libintl_dgettext", referenced from:
  "_libintl_gettext", referenced from:
      __locale_gettext in libpython3.10.a(_localemodule.o)
      __locale_dgettext in libpython3.10.a(_localemodule.o)
  "_libintl_setlocale", referenced from:
  "_libintl_gettext", referenced from:
      __locale_setlocale in libpython3.10.a(_localemodule.o)
      __locale_localeconv in libpython3.10.a(_localemodule.o)
      __locale_gettext in libpython3.10.a(_localemodule.o)
  "_libintl_textdomain", referenced from:
  "_libintl_setlocale", referenced from:
      __locale_textdomain in libpython3.10.a(_localemodule.o)
      __locale_setlocale in libpython3.10.a(_localemodule.o)
      __locale_localeconv in libpython3.10.a(_localemodule.o)
  "_libintl_textdomain", referenced from:
      __locale_textdomain in libpython3.10.a(_localemodule.o)
ld: symbol(s) not found for architecture x86_64
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [Programs/_testembed] Error 1
make: *** Waiting for unfinished jobs....
make: *** [python.exe] Error 1

BUILD FAILED (OS X 11.5.1 using python-build 2.3.2-7-g16f7ea03)

Inspect or clean up the working tree at /var/folders/bz/qdc41tl10s36tg71w9qdq5jh0000gn/T/python-build.20220727103447.34041
Results logged to /var/folders/bz/qdc41tl10s36tg71w9qdq5jh0000gn/T/python-build.20220727103447.34041.log

Last 10 log lines:
      __locale_localeconv in libpython3.10.a(_localemodule.o)
  "_libintl_textdomain", referenced from:
      __locale_textdomain in libpython3.10.a(_localemodule.o)
ld: symbol(s) not found for architecture x86_64
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [Programs/_testembed] Error 1
make: *** Waiting for unfinished jobs....
make: *** [python.exe] Error 1
```
[确保安装了 Python 的二进制依赖项和构建工具。](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
[遇到编译失败，可以参考官方提供的解决方案 Common-build-problems](https://github.com/pyenv/pyenv/wiki/Common-build-problems)

只需为命令添加前缀：AR=/usr/bin/env pyenv install .... 这AR为调用pyenv. 或者（暂时）brew uninstall binutils，如果那是ar从哪里来的（你可以检查which ar——如果它说/usr/local/bin/ar你可能已经安装了 binutils）。
```
$ which ar
/usr/bin/ar
```

```
env PYTHON_CONFIGURE_OPTS="--enable-framework --enable-universalsdk --with-universal-archs=universal2" pyenv install 3.10.5   
python-build: use openssl@1.1 from homebrew
python-build: use readline from homebrew
Installing Python-3.10.5...
python-build: use tcl-tk from homebrew
python-build: use readline from homebrew
python-build: use zlib from xcode sdk

BUILD FAILED (OS X 12.5 using python-build 2.3.2-7-g16f7ea03)

Inspect or clean up the working tree at /var/folders/bz/qdc41tl10s36tg71w9qdq5jh0000gn/T/python-build.20220729155015.61546
Results logged to /var/folders/bz/qdc41tl10s36tg71w9qdq5jh0000gn/T/python-build.20220729155015.61546.log

Last 10 log lines:
  "_libintl_gettext", referenced from:
      __locale_gettext in libpython3.10.a(_localemodule.o)
  "_libintl_setlocale", referenced from:
      __locale_setlocale in libpython3.10.a(_localemodule.o)
      __locale_localeconv in libpython3.10.a(_localemodule.o)
  "_libintl_textdomain", referenced from:
      __locale_textdomain in libpython3.10.a(_localemodule.o)
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [Python.framework/Versions/3.10/Python] Error 1
```
**重要**
下面安装成功`先安装了arch -arm64 brew install pyenv-virtualenv`然后配置了`.zshrc`和`.zprofile`
## .zshrc
```
$ cat ~/.zshrc
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
## .zprofile
```
$ cat ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
eval "$(/opt/homebrew/bin/brew shellenv)"

# Created by `pipx` on 2021-09-17 05:33:24
export PATH="$PATH:/Users/matias/.local/bin"
eval "$(/opt/homebrew/bin/brew shellenv)"
pyenv主要看下面几个
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```
安装`python 3.10.5`
```
$ arch -arm64 pyenv install 3.10.5
python-build: use openssl@1.1 from homebrew
python-build: use readline from homebrew
Installing Python-3.10.5...
python-build: use tcl-tk from homebrew
python-build: use readline from homebrew
python-build: use zlib from xcode sdk
Installed Python-3.10.5 to /Users/matias/.pyenv/versions/3.10.5
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

```
$ arch -arm64 brew install pyenv-virtualenv
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//m4-1.4.19.arm64_monterey.bottle.tar.gz
######################################################################## 100.0%
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//autoconf-2.71.arm64_monterey.bottle.tar.gz
######################################################################## 100.0%
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//pkg-config-0.29.2_3.arm64_monterey.bottle.tar.gz
######################################################################## 100.0%
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//pyenv-2.3.2.arm64_monterey.bottle.tar.gz
######################################################################## 100.0%
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles//pyenv-virtualenv-1.1.5.all.bottle.tar.gz
######################################################################## 100.0%
==> Installing dependencies for pyenv-virtualenv: m4, autoconf, pkg-config and pyenv
==> Installing pyenv-virtualenv dependency: m4
==> Pouring m4-1.4.19.arm64_monterey.bottle.tar.gz
🍺  /opt/homebrew/Cellar/m4/1.4.19: 13 files, 742.3KB
==> Installing pyenv-virtualenv dependency: autoconf
==> Pouring autoconf-2.71.arm64_monterey.bottle.tar.gz
🍺  /opt/homebrew/Cellar/autoconf/2.71: 71 files, 3.2MB
==> Installing pyenv-virtualenv dependency: pkg-config
==> Pouring pkg-config-0.29.2_3.arm64_monterey.bottle.tar.gz
🍺  /opt/homebrew/Cellar/pkg-config/0.29.2_3: 11 files, 676.3KB
==> Installing pyenv-virtualenv dependency: pyenv
==> Pouring pyenv-2.3.2.arm64_monterey.bottle.tar.gz
🍺  /opt/homebrew/Cellar/pyenv/2.3.2: 930 files, 3MB
==> Installing pyenv-virtualenv
==> Pouring pyenv-virtualenv-1.1.5.all.bottle.tar.gz
==> Caveats
To enable auto-activation add to your profile:
  if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi
==> Summary
🍺  /opt/homebrew/Cellar/pyenv-virtualenv/1.1.5: 22 files, 66.2KB
==> Running `brew cleanup pyenv-virtualenv`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Caveats
==> pyenv-virtualenv
To enable auto-activation add to your profile:
  if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi
```

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

# 安装

2 安装
安装有两种方式：

自动安装
手动安装
2.1 自动安装
curl https://pyenv.run | bash
# 或
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
1
2
3
2.2 手动安装
手动安装大致分为三步：

安装pyenv
配置环境变量
初始化
2.2.1 安装pyenv
笔者系统Manjaro，可以直接yay安装：

yay -S pyenv
1
其他系统的可以使用apt search/yum search等看看软件包仓库有没有，有的话直接安装即可，没有的话，可以clone安装：

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
1
（这一步是可选的）接着就是编译动态bash扩展进行加速：

cd ~/.pyenv && src/configure && make -C src
1
官方解释说，不用害怕编译失败，因为仍然会正常工作。

2.2.2 配置环境变量
这一步就是把PYENV以及更新后的PATH配置成环境变量，官方文档按照shell类型进行了分类，根据自己情况选择即可。

2.2.2.1 bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
1
2
2.2.2.2 Zsh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
1
2
2.2.2.3 Fish shell
set -Ux PYENV_ROOT $HOME/.pyenv
set -Ux fish_user_paths $PYENV_ROOT/bin $fish_user_paths
1
2
2.2.3 初始化
配置完环境变量后还要进行初始化操作，文档同样按shell类型进行了分类。

2.2.3.1 bash
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
1
2.2.3.2 Zsh
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
1
2.2.3.3 Fish shell
echo -e '\n\n# pyenv init\nif command -v pyenv 1>/dev/null 2>&1\n  pyenv init - | source\nend' >> ~/.config/fish/config.fish
1
2.3 测试
重新开启一个终端，输入pyenv，输出如下信息就表明安装成功了