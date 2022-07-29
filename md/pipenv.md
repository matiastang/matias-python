<!--
 * @Author: matiastang
 * @Date: 2022-07-26 15:31:08
 * @LastEditors: matiastang
 * @LastEditTime: 2022-07-29 16:34:20
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