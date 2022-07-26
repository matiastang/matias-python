<!--
 * @Author: matiastang
 * @Date: 2022-07-26 15:17:44
 * @LastEditors: matiastang
 * @LastEditTime: 2022-07-26 15:34:33
 * @FilePath: /matias-python/md/pipx.md
 * @Description: pipx
-->
# pipx

[pipx](https://pypi.org/project/pipx/)
[pipx](https://zhuanlan.zhihu.com/p/330676831)

`pipx` 是一种帮助您安装和运行用 `Python` 编写的最终用户应用程序的工具。它大致类似于 `macOS` 的`brew`、`JavaScript` 的`npx`和 `Linux` 的`apt`.

它与 `pip` 密切相关。事实上，它使用 `pip`，但专注于安装和管理可以直接作为应用程序从命令行运行的 `Python` 包。

```
brew install pipx
```

提示：Error opening archive: Failed to open

[issues/11209](https://github.com/Homebrew/brew/issues/11209)

更新`brew`：`brew update`
后再：`brew install pipx`

* 查看版本

```
$ pipx --version
0.16.4
```

```
$ pipx list
venvs are in /Users/matias/.local/pipx/venvs
apps are exposed on your $PATH at /Users/matias/.local/bin
   package pipenv 2021.5.29, Python 3.9.7
    - pipenv
    - pipenv-resolver
```
