<!--
 * @Author: matiastang
 * @Date: 2022-07-26 14:54:18
 * @LastEditors: matiastang
 * @LastEditTime: 2022-07-26 15:17:08
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