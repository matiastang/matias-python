<!--
 * @Author: matiastang
 * @Date: 2022-07-26 14:54:18
 * @LastEditors: matiastang
 * @LastEditTime: 2023-03-07 19:32:57
 * @FilePath: /matias-python/md/pip3.md
 * @Description: pip3
-->
# pip3

`pip3` 是 `Python3.x` 包管理工具，该工具提供了对`Python3.x` 包的查找、下载、安装、卸载的功能。
**注意**：`Python 2.7.9 +` 或 `Python 3.4+` 以上版本都自带 `pip` 工具。

* 查看`python3`版本

```
$ python3 --version
Python 3.8.9
```

* 查看`pip3`版本(`Python3.x` 版本命令)

```
$ pip3 -V
$ pip3 --version
```

## 安装pip3

在`python3.x`的路径下
```
curl https://bootstrap.pypa.io/get-pip.py | python3
```
```sh
$ curl https://bootstrap.pypa.io/get-pip.py | python3      
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 2573k  100 2573k    0     0  1323k      0  0:00:01  0:00:01 --:--:-- 1322k
Defaulting to user installation because normal site-packages is not writeable
Collecting pip
  Downloading pip-23.3.2-py3-none-any.whl.metadata (3.5 kB)
Collecting setuptools
  Downloading setuptools-69.0.2-py3-none-any.whl.metadata (6.3 kB)
Collecting wheel
  Downloading wheel-0.42.0-py3-none-any.whl.metadata (2.2 kB)
Downloading pip-23.3.2-py3-none-any.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 1.6 MB/s eta 0:00:00
Downloading setuptools-69.0.2-py3-none-any.whl (819 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 819.5/819.5 kB 272.2 kB/s eta 0:00:00
Downloading wheel-0.42.0-py3-none-any.whl (65 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 65.4/65.4 kB 177.8 kB/s eta 0:00:00
Installing collected packages: wheel, setuptools, pip
  WARNING: The script wheel is installed in '/home/tdy/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts pip, pip3 and pip3.10 are installed in '/home/tdy/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-23.3.2 setuptools-69.0.2 wheel-0.42.0
```
`zsh`中添加如下配置
```sh
# pip3
export PATH="/home/tdy/.local/bin:$PATH"
```
* 刷新
```sh
source .zshrc
tdy@tangdaoyong ~ % pip3 -V
pip 23.3.2 from /home/tdy/.local/lib/python3.10/site-packages/pip (python 3.10)
```
查看相应的包
```
pip3 list
```
安装和更新pip3
```
pip3 install --upgrade pip3
```
```
$ pip3 --version
pip 22.2 from /Library/Python/3.8/site-packages/pip (python 3.8)
```
```
$ pip3 list
Package          Version
---------------- -------
pip              22.2
powerline-status 2.7
setuptools       49.2.1
six              1.15.0
wheel            0.33.1
```

## 使用pip3 install 包太慢

添加文件系统地址
```
pip3 install matplotlib -i https://pypi.douban.com/simple
```
```sh
$ pip3 install itemadapter -i https://pypi.tuna.tsinghua.edu.cn/simple
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting itemadapter
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/f0/42/1e15e8186bf2d1b1990f6bac30f77d98a3b54084ecf4e19c25803d0a4713/itemadapter-0.7.0-py3-none-any.whl (10 kB)
Installing collected packages: itemadapter
Successfully installed itemadapter-0.7.0
```

## 安装`arch -arm64`包

```
$ arch -arm64 pip3 install *** 
```