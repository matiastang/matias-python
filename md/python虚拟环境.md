<!--
 * @Author: matiastang
 * @Date: 2023-12-12 17:45:33
 * @LastEditors: matiastang
 * @LastEditTime: 2023-12-12 18:36:34
 * @FilePath: /matias-python/md/python虚拟环境.md
 * @Description: python虚拟环境
-->
# python虚拟环境

python有3个模块可以用于创建和管理python虚拟环境：

* venv
* virtualenv
* pyenv

其中，venv模块是Python3.3之后标准库自带的虚拟环境创建和管理工具，在一定程度上能够替代virtualenv。但venv是Python3.3才有的，Python2.X不能使用，而virtualenv同时支持Python2.X和Python3.X，特别是在当前的生产环境中Python2.X还占有很大比例的情况下我们依然需要virtualenv。

## pyenv

`pyenv` 主要用来对 `Python` 解释器进行管理，可以管理系统上的多个版本的 `Python` 解释器。它的主要原理就是将新的解释器路径放在 `PATH` 环境变量的前面，这样新的 `python` 程序就“覆盖”了老的 `python` 程序，达到了切换解释器的目的。

`pyenv-virtualenv`虚拟环境管理也是一样，`shims`管理各个虚拟环境命令的路径，然后再将`shims`路径插入到系统环境变量最前面，达到切换虚拟环境的目的。

### pyenv 创建虚拟环境

安装`pyenv-virtualenv`
`pyenv`要使用虚拟环境管理，必须安装一个插件`pyenv-virtualenv`

```sh
git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
source ~/.bash_profile
```

查看是否安装成功：

```sh
$ pyenv help virtualenv
Usage: pyenv virtualenv [-f|--force] [VIRTUALENV_OPTIONS] [version] <virtualenv-name>
       pyenv virtualenv --version
       pyenv virtualenv --help

  -f/--force       Install even if the version appears to be installed already
```

* 虚拟环境创建与切换
使用pyenv创建虚拟环境（不需要指定目录）
```sh
# 直接创建虚拟环境myproj3，它不需要指定目录，不会在当前目录生成myproj3目录文件
$ pyenv virtualenv 3.10.5 huggingface3.10.5
```

查看虚拟环境列表：
```sh
$ pyenv virtualenvs
  3.10.5/envs/huggingface3.10.5 (created from /Users/matias/.pyenv/versions/3.10.5)
  huggingface3.10.5 (created from /Users/matias/.pyenv/versions/3.10.5)
```

激活虚拟环境
```sh
$ pyenv activate huggingface3.10.5
pyenv-virtualenv: prompt changing will be removed from future release. configure `export PYENV_VIRTUALENV_DISABLE_PROMPT=1' to simulate the behavior.
```

退出虚拟环境
```sh
$ pyenv deactivate
```

删除虚拟环境
```sh
# 直接卸载该环境
$ pyenv uninstall huggingface3.10.5
```
