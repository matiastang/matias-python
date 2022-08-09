<!--
 * @Author: matiastang
 * @Date: 2022-07-26 15:31:08
 * @LastEditors: matiastang
 * @LastEditTime: 2022-08-09 17:36:15
 * @FilePath: /matias-python/md/pipenv.md
 * @Description: pipenv
-->
# pipenv

[pipenv 使用](https://cdn.modb.pro/db/29564)

`Python.org` 推荐的名为 `Pipenv` 的 `Python` 包管理器也可以用来安装 `Python` 应用。与 `Pip` 不同，`Pipenv` 默认会自动创建虚拟环境。这意味着你不再需要为项目手动创建虚拟环境。

`Pipfile` 与 `Pipfile.lock` 是社区拟定的依赖管理文件，用于替代过于简陋的 `requirements.txt` 文件. 过去大家经常使用`virtualenv`来创建虚拟环境，通过`pip freeze`生成`requirements.txt`文件，然后通过`pip install -r requirements.txt`进行项目模块的管理与安装。这样的安装存在很多问题，比如每次更新模块后，需要手动的重新生成依赖文件，等等问题
* 安装
```
pipx install pipenv
```
* 添加环境变量
```
pipx ensurepath
```
* 刷新
```
source ~/.zshrc
```
* 查看版本
```
$ pipenv --version
pipenv, version 2021.5.29
```

## 创建虚拟环境

Pipenv的作用

可以利用pipenv来实现同时管理项目中的python虚拟环境和相关包依赖。

使用步骤

cmd中输入命令 pip install pipenv 安装pipenv
cmd切换路径到需要建立虚拟环境的项目目录下
输入命令 pipenv install 开始安装虚拟环境
安装完毕后输入命令 pipenv shell 进入虚拟环境
Pipfile文件

虚拟环境安装完毕后项目目录中将创建Pipfile/Pipfile.lock两个文件
Pipfile：用于保存项目的python版本、依赖包等相关信息
Pipfile.lock：用于对Pipfile的锁定
Pipfile文件可以单独移放到其他项目内，用于项目虚拟环境的建立和依赖包的安装
常用命令

pipenv install：
若项目目录中虚拟环境未创建且无Pipfile文件，将安装虚拟环境并创建Pipfile文件
若项目目录中虚拟环境未创建且有Pipfile文件，将根据Pipfile文件来安装相应python版本和依赖包
若项目目录中虚拟环境已创建且有Pipfile文件，将根据Pipfile文件来安装依赖包

pipenv install xx:：安装python包
pipenv uninstall xx:：卸载python包
pipenv shell：进入虚拟环境(项目目录下)
exit：退出虚拟环境
pipenv graph：显示包依赖关系
pipenv --venv：显示虚拟环境安装路径
执行 pipenv lock --clear 用于清空依赖缓存

## 换源

`pipenv install ***`安装报错`ReadTimeoutError`

是因为`pip`下载源默认设置为国外

解决办法是：

将`pip`下载源切换为国内地址：index-url = https://pypi.tuna.tsinghua.edu.cn/simple
修改当前目录下Pipfile文件，将[source]下的url属性改成国内的源即可：
```
[[source]]
url = "https://mirrors.aliyun.com/pypi/simple"
verify_ssl = true
name = "pypi"
```
## 问题

### `python`的版本问题导致`Locking Failed!`
```
Running $ pipenv lock then $ pipenv sync.
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✘ Locking Failed! 
```

[stackoverflow](https://stackoverflow.com/questions/58280484/ssl-module-in-python-is-not-available-on-osx/60467942#60467942)

`python`版本使用不对造成的
```
$ pipx list
venvs are in /Users/matias/.local/pipx/venvs
apps are exposed on your $PATH at /Users/matias/.local/bin
   package pipenv 2022.8.5, installed using Python 3.9.7
    - pipenv
    - pipenv-resolver
```
```
cd /Users/matias/.local/pipx/venvs 
(base)  ~/.local/pipx/venvs  ll
total 0
drwxr-xr-x  7 matias  staff   224B  9 17  2021 pipenv
(base)  ~/.local/pipx/venvs  cd pipenv 
(base)  ~/.local/pipx/venvs/pipenv  ll
total 16
drwxr-xr-x  13 matias  staff   416B  8  9 16:07 bin
drwxr-xr-x   2 matias  staff    64B  9 17  2021 include
drwxr-xr-x   3 matias  staff    96B  9 17  2021 lib
-rw-r--r--   1 matias  staff   1.3K  8  9 16:07 pipx_metadata.json
-rw-r--r--   1 matias  staff    93B  9 17  2021 pyvenv.cfg
(base)  ~/.local/pipx/venvs/pipenv  cat pyvenv.cfg 
以前的配置，其中python用的3.9.7和当前环境使用的不一样，当前环境使用的是`pyenv`安装的`python`，应该是`pipx`安装`pipenv`时，还没有引入`pyenv`管理版本。
home = /opt/homebrew/opt/python@3.9/bin
include-system-site-packages = false
version = 3.9.7
(base)  ~/.local/pipx/venvs/pipenv  which python3
/Users/matias/.pyenv/shims/python3
```
修改`pipenv`配置文件
```
(base)  ~/.local/pipx/venvs/pipenv  vim pyvenv.cfg 
(base)  ~/.local/pipx/venvs/pipenv  cat pyvenv.cfg 
home = /Users/matias/.pyenv/shims/python3
include-system-site-packages = false
version = 3.10.5
```
重新添加则成功了
```
pipenv install Scrapy
Installing Scrapy...
Adding Scrapy to Pipfile's [packages]...
✔ Installation Succeeded 
Pipfile.lock not found, creating...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success! 
Updated Pipfile.lock (9ff1f9)!
Installing dependencies from Pipfile.lock (9ff1f9)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 1/1 — 00:00:00
```

### `ERROR:: --system is`

```
pipenv --python 3.10                               
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

ERROR:: --system is intended to be used for pre-existing Pipfile installation, not installation of specific packages. Aborting.
```
可以先用rm（删除虚拟环境）清除之前的操作，再重新install：
```
$ pipenv --rm
Removing virtualenv (/Users/matias/.local/share/virtualenvs/welfare-lottery-scrapy-Qkb1Kj8J)...
(mt_scrapy)  ~/matias/MT/MTGithub/scrapy/welfare-lottery-scrapy   main ±  pipenv install
Creating a virtualenv for this project...
Pipfile: /Users/matias/matias/MT/MTGithub/scrapy/welfare-lottery-scrapy/Pipfile
Using /Users/matias/.pyenv/versions/3.10.5/bin/python3 (3.10.5) to create virtualenv...
⠸ Creating virtual environment...created virtual environment CPython3.10.5.final.0-64 in 181ms
  creator CPython3Posix(dest=/Users/matias/.local/share/virtualenvs/welfare-lottery-scrapy-Qkb1Kj8J, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/matias/Library/Application Support/virtualenv)
    added seed packages: pip==22.1.2, setuptools==63.1.0, wheel==0.37.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment! 
Virtualenv location: /Users/matias/.local/share/virtualenvs/welfare-lottery-scrapy-Qkb1Kj8J
Creating a Pipfile for this project...
Pipfile.lock not found, creating...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Updated Pipfile.lock (e4eef2)!
Installing dependencies from Pipfile.lock (e4eef2)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```