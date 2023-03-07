<!--
 * @Author: matiastang
 * @Date: 2022-07-26 14:51:42
 * @LastEditors: matiastang
 * @LastEditTime: 2023-03-07 09:59:35
 * @FilePath: /matias-python/md/pip.md
 * @Description: pip
-->
# pip

`pip` 是 `Python2.x` 包管理工具，该工具提供了对`Python2.x` 包的查找、下载、安装、卸载的功能。
**注意**：`Python 2.7.9 +` 或 `Python 3.4+` 以上版本都自带 `pip` 工具。

* 查看`python`版本

```
$ python --version
Python 2.7.16
```

* 查看`pip`版本(`Python2.x` 版本命令)

```
$ pip -V
$ pip --version
```

## 安装pip

```
sudo easy_install pip
```
这个会默认安装`pip2`
`pip`是`python`的包管理工具，在`Python2.7`的安装包中，`easy_install.py`是默认安装的，而`pip`需要我们手动安装。
打开终端：
```
sudo easy_install pip
```
查看版本
```
pip --version
```
安装和更新pip
```
pip install --upgrade pip
```

## sudo easy_install pip 报错

* 使用sudo easy_install pip命令在Mac终端安装pip时报错，如下：
  
```
$ sudo easy_install pip
Password:
Searching for pip
Reading https://pypi.org/simple/pip/
Downloading https://files.pythonhosted.org/packages/cd/b6/cf07132d631444dd7ce0ed199f2327eb34e2418f1675145e5b10e1ee65cd/pip-22.2.tar.gz#sha256=8d63fcd4ee293e30b644827268a0a973d080e5c7425ef26d427f5eb2126c7681
Best match: pip 22.2
Processing pip-22.2.tar.gz
Writing /tmp/easy_install-ID2zPf/pip-22.2/setup.cfg
Running pip-22.2/setup.py -q bdist_egg --dist-dir /tmp/easy_install-ID2zPf/pip-22.2/egg-dist-tmp-1rUwbJ
Traceback (most recent call last):
  File "/usr/bin/easy_install", line 13, in <module>
    load_entry_point('setuptools==41.0.1', 'console_scripts', 'easy_install')()
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/command/easy_install.py", line 2316, in main
    **kw
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/__init__.py", line 145, in setup
    return distutils.core.setup(**attrs)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/core.py", line 151, in setup
    dist.run_commands()
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py", line 953, in run_commands
    self.run_command(cmd)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py", line 972, in run_command
    cmd_obj.run()
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/command/easy_install.py", line 418, in run
    self.easy_install(spec, not self.no_deps)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/command/easy_install.py", line 679, in easy_install
    return self.install_item(spec, dist.location, tmpdir, deps)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/command/easy_install.py", line 705, in install_item
    dists = self.install_eggs(spec, download, tmpdir)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/command/easy_install.py", line 890, in install_eggs
    return self.build_and_install(setup_script, setup_base)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/command/easy_install.py", line 1158, in build_and_install
    self.run_setup(setup_script, setup_base, args)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/command/easy_install.py", line 1144, in run_setup
    run_setup(setup_script, args)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/sandbox.py", line 253, in run_setup
    raise
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/contextlib.py", line 35, in __exit__
    self.gen.throw(type, value, traceback)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/sandbox.py", line 195, in setup_context
    yield
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/contextlib.py", line 35, in __exit__
    self.gen.throw(type, value, traceback)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/sandbox.py", line 166, in save_modules
    saved_exc.resume()
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/sandbox.py", line 141, in resume
    six.reraise(type, exc, self._tb)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/sandbox.py", line 154, in save_modules
    yield saved
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/sandbox.py", line 195, in setup_context
    yield
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/sandbox.py", line 250, in run_setup
    _execfile(setup_script, ns)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/setuptools/sandbox.py", line 44, in _execfile
    code = compile(script, filename, 'exec')
  File "/tmp/easy_install-ID2zPf/pip-22.2/setup.py", line 7
    def read(rel_path: str) -> str:
                     ^
SyntaxError: invalid syntax
```

在终端依次输入：
```
$ curl https://bootstrap.pypa.io/pip/get-pip.py -o get-pip.py
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 2500k  100 2500k    0     0  15502      0  0:02:45  0:02:45 --:--:-- 10678
```
```
$ sudo python3 get-pip.py
Password:
WARNING: The directory '/Users/matias/Library/Caches/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Collecting pip
  Downloading pip-22.2-py3-none-any.whl (2.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 21.5 kB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.2.3
    Uninstalling pip-20.2.3:
      Successfully uninstalled pip-20.2.3
Successfully installed pip-22.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
```
```
$ pip --version
pip 22.2 from /Library/Python/3.8/site-packages/pip (python 3.8)
```
```
$ pip list
Package          Version
---------------- -------
pip              22.2
powerline-status 2.7
setuptools       49.2.1
six              1.15.0
wheel            0.33.1
```

## 使用镜像地址

```sh
$ pip3 install apscheduler -i https://pypi.tuna.tsinghua.edu.cn/simple
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting apscheduler
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/d0/08/952d9570f4897dc2b30166fca5afd3a2cd19b3d408abdb470978484e8a09/APScheduler-3.10.1-py3-none-any.whl (59 kB)
     |████████████████████████████████| 59 kB 1.7 MB/s
Collecting tzlocal!=3.*,>=2.0
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/31/b7/3bc2c1868f27677139b772e4fde95265b93151912fd90eb874827943bfcf/tzlocal-4.2-py3-none-any.whl (19 kB)
Requirement already satisfied: six>=1.4.0 in /usr/lib/python3/dist-packages (from apscheduler) (1.14.0)
Collecting pytz
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/2e/09/fbd3c46dce130958ee8e0090f910f1fe39e502cc5ba0aadca1e8a2b932e5/pytz-2022.7.1-py2.py3-none-any.whl (499 kB)
     |████████████████████████████████| 499 kB 920 kB/s
Requirement already satisfied: setuptools>=0.7 in /usr/lib/python3/dist-packages (from apscheduler) (45.2.0)
Collecting pytz-deprecation-shim
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/eb/73/3eaab547ca809754e67e06871cff0fc962bafd4b604e15f31896a0f94431/pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl (15 kB)
Collecting backports.zoneinfo; python_version < "3.9"
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/1a/ab/3e941e3fcf1b7d3ab3d0233194d99d6a0ed6b24f8f956fc81e47edc8c079/backports.zoneinfo-0.2.1-cp38-cp38-manylinux1_x86_64.whl (74 kB)
     |████████████████████████████████| 74 kB 859 kB/s
Collecting tzdata; python_version >= "3.6"
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/fa/5e/f99a7df3ae2079211d31ec23b1d34380c7870c26e99159f6e422dcbab538/tzdata-2022.7-py2.py3-none-any.whl (340 kB)
     |████████████████████████████████| 340 kB 2.3 MB/s
Installing collected packages: tzdata, backports.zoneinfo, pytz-deprecation-shim, tzlocal, pytz, apscheduler
Successfully installed apscheduler-3.10.1 backports.zoneinfo-0.2.1 pytz-2022.7.1 pytz-deprecation-shim-0.1.0.post0 tzdata-2022.7 tzlocal-4.2
```

pip install -i 国内镜像地址 包名

例如： pip install -i  https://mirrors.aliyun.com/pypi/simple/ numpy



国内常用源镜像地址：

清华：https://pypi.tuna.tsinghua.edu.cn/simple

阿里云：http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

华中理工大学：http://pypi.hustunique.com/

山东理工大学：http://pypi.sdutlinux.org/ 

豆瓣：http://pypi.douban.com/simple/

note：新版ubuntu要求使用https源，要注意

生成: pip freeze > requirements.txt 

导入: pip install -r requirements.txt