<!--
 * @Author: matiastang
 * @Date: 2022-08-01 14:59:56
 * @LastEditors: matiastang
 * @LastEditTime: 2023-03-07 19:26:22
 * @FilePath: /matias-python/md/miniforge安装.md
 * @Description: 
-->
# miniforge

mac用的是Pyenv, 我的windows电脑使用Anaconda, linux服务器用miniconda

Anaconda庞大, 全面. 从下载安装到完全配置好可能需要半个小时甚至更长. 但你不需要考虑包之间依赖关系. 不同的环境(例如不同的python版本, 或者是不同语言)的切换, 到一般来说是命令行启动的一众app(例如Jupyter, Spyder)都是GUI, 操作傻瓜上手快. 

Miniconda是部署最快的了, linux服务器登陆上去后, wget一个miniconda.sh, 从安装到开始把代码推送过去开始运行可能只需要几分钟. 

Pyenv非常轻量, 和miniconda类似. 但pyenv只管不同的python环境, 还可以配合pyenv-virtualenv. pyenv后, python的包管理器还是pip, 在数据科学领域, pip也能实现几乎所有安装, 但conda已成为默认选项. 

如果是纯小白, 且系统硬盘不吃紧 -- anaconda
但凡有经验, 喜欢自己配置环境的 -- miniconda
如果pip习惯了, 或者从其他语言(例如rbenv)跳过来的话. 了解这一套env怎么用的 -- pyenv

[miniforge官网](https://github.com/conda-forge/miniforge)
```sh
$ echo $PATH
```

重新初始化 shell 环境，执行如下命令

```sh
exec $SHELL
```

* `conda list`确认安装了哪个软件包
```sh

```
* `conda env list`或`conda info -e`确认当前存在什么虚拟环境
```sh
$ conda env list
# conda environments:
#
base                  *  /opt/homebrew/Caskroom/miniforge/base
mt_scrapy                /opt/homebrew/Caskroom/miniforge/base/envs/mt_scrapy
mt_tensorflow            /opt/homebrew/Caskroom/miniforge/base/envs/mt_tensorflow
my_scrapy_3.8.10         /opt/homebrew/Caskroom/miniforge/base/envs/my_scrapy_3.8.10
```
* `conda update conda`检查更新当前`conda`
```sh

```
* `conda create -n 虚拟环境名称 python=版本号`创建一个虚拟环境，同时设置`python`版本。如：`conda create -n tensorflow python=3.8`
```sh
$ conda create -n mt_tensorflow python=3.10
#
# To activate this environment, use
#
#     $ conda activate mt_tensorflow
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

* 激活
```sh
 $ conda activate 虚拟环境名称
```

* 退出
```sh
$ conda deactivate
```

## 安装miniforge

```sh
$ brew install miniforge
...
Linking Binary 'conda' to '/opt/homebrew/bin/conda'
🍺  miniforge was successfully installed!
```
**注意**安装完成后重启终端
此时就可以使用`conda install`安装所需库了，比如`pandas`，输入`conda install pandas`就会帮你自动安装此库
## 使用GitHub中的命令下载
```sh
$ curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh
```
`MD5`校验不通过
```sh
WARNING: md5sum mismatch of tar archive
expected: 930549447a7f4eaccee4012682365a91
     got: 2af142c23775ff3818e88cc9e0420286
Unpacking payload ...
```
## 下载慢可以用国内的镜像地址

[镜像地址](https://repo.anaconda.com/archive/)

## 更换镜像源

确实现在`miniforge`我们已安装成功，并能正常使用，但对于国内用户来讲，下载速度实在是太慢了，我们需更改其默认镜像源，比如我将其改为清华镜像源进行下载，那下载速度简直不要太快
首先打开终端，输入以下命令
```
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
$ conda config --set show_channel_urls yes
```
确认更改`conda help`可以看到`config`的地址，默认为
```
$ conda help
...
config       Modify configuration values in .condarc. This is modeled after the git config command. Writes to the user
                 .condarc file (/Users/matias/.condarc) by default.
...
```
```
$ cat ./condarc
```

## 创建虚拟环境

用`conda`创建一个虚拟环境，同时设置`python`版本
`conda create -n 虚拟环境名称 python=版本号`
`conda create -n tensorflow python=3.8`
```
$ conda create -n mt_tensorflow python=3.10
...
#
# To activate this environment, use
#
#     $ conda activate mt_tensorflow
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

## 激活虚拟环境

`conda activate 虚拟环境名`
`conda activate tensorflow`
**提示**如果需要取消激活状态，输入`conda deactivate`即可
```
$ conda activate mt_tensorflow

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.
```
```
$ conda init
no change     /opt/homebrew/Caskroom/miniforge/base/condabin/conda
no change     /opt/homebrew/Caskroom/miniforge/base/bin/conda
no change     /opt/homebrew/Caskroom/miniforge/base/bin/conda-env
no change     /opt/homebrew/Caskroom/miniforge/base/bin/activate
no change     /opt/homebrew/Caskroom/miniforge/base/bin/deactivate
no change     /opt/homebrew/Caskroom/miniforge/base/etc/profile.d/conda.sh
no change     /opt/homebrew/Caskroom/miniforge/base/etc/fish/conf.d/conda.fish
no change     /opt/homebrew/Caskroom/miniforge/base/shell/condabin/Conda.psm1
no change     /opt/homebrew/Caskroom/miniforge/base/shell/condabin/conda-hook.ps1
no change     /opt/homebrew/Caskroom/miniforge/base/lib/python3.9/site-packages/xontrib/conda.xsh
no change     /opt/homebrew/Caskroom/miniforge/base/etc/profile.d/conda.csh
modified      /Users/matias/.bash_profile

==> For changes to take effect, close and re-open your current shell. <==
```
`zsh`初始化
```
$ conda init zsh
no change     /opt/homebrew/Caskroom/miniforge/base/condabin/conda
no change     /opt/homebrew/Caskroom/miniforge/base/bin/conda
no change     /opt/homebrew/Caskroom/miniforge/base/bin/conda-env
no change     /opt/homebrew/Caskroom/miniforge/base/bin/activate
no change     /opt/homebrew/Caskroom/miniforge/base/bin/deactivate
no change     /opt/homebrew/Caskroom/miniforge/base/etc/profile.d/conda.sh
no change     /opt/homebrew/Caskroom/miniforge/base/etc/fish/conf.d/conda.fish
no change     /opt/homebrew/Caskroom/miniforge/base/shell/condabin/Conda.psm1
no change     /opt/homebrew/Caskroom/miniforge/base/shell/condabin/conda-hook.ps1
no change     /opt/homebrew/Caskroom/miniforge/base/lib/python3.9/site-packages/xontrib/conda.xsh
no change     /opt/homebrew/Caskroom/miniforge/base/etc/profile.d/conda.csh
modified      /Users/matias/.zshrc

==> For changes to take effect, close and re-open your current shell. <==
```
激活虚拟环境，取消激活状态使用`conda deactivate`
```
(base)  ~  $ conda activate mt_tensorflow
(mt_tensorflow)  ~ 
```
```
(mt_tensorflow)  ~  which python3
/opt/homebrew/Caskroom/miniforge/base/envs/mt_tensorflow/bin/python3
(mt_tensorflow)  ~  which python
/opt/homebrew/Caskroom/miniforge/base/envs/mt_tensorflow/bin/python
(mt_tensorflow)  ~  which pip3
/opt/homebrew/Caskroom/miniforge/base/envs/mt_tensorflow/bin/pip3
(mt_tensorflow)  ~  which pip
/opt/homebrew/Caskroom/miniforge/base/envs/mt_tensorflow/bin/pip
(mt_tensorflow)  ~  pip3 install tensorflow-macos
Collecting tensorflow-macos
```
## 安装tensorflow

当创建完虚拟环境后，做完准备工作之后，我们需要安装tensorflow-macos，这是我们真正的目的。下载`tensorflow`安装包（支持arm架构版本的）
下载慢
```
$ pip3 install tensorflow-macos
```
使用下面的下载
```
pip3 install tensorflow-macos -i https://pypi.douban.com/simple
pip3 install tensorflow-metal -i https://pypi.douban.com/simple
```
1. 测试`tensorflow`
```
$ python3 /Users/matias/matias/MT/MTGithub/matias-TensorFlow/src/python/tensorflow_install_test.py
2.9.2
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU'), PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```
2. VSCode配置
```py
import tensorflow as tf
# 编辑器提示：Import "tensorflow" could not be resolvedPylancereportMissingImports
```
下载了`tensorflow`还有上述提示，则说明你配置了多个`python`环境，而编辑器目前所在的`python`环境没有下载该包，可以选择更换编辑器环境或者重新在编辑器的环境下下载。
更换环境步骤：`ctrl+shift+p` -->输入：`python:select interpreter`选择下载了该包的环境。

* 在`conda`的虚拟环境中查看`python3`的地址：
```
(mt_tensorflow)  ~  which python3
/opt/homebrew/Caskroom/miniforge/base/envs/mt_tensorflow/bin/python3
```
点击`Enter interpreter Path`将上面地址添加进去