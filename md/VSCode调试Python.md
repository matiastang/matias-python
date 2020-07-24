<!--
 * @Descripttion: 
 * @version: 
 * @Author: sueRimn
 * @Date: 2020-07-09 10:09:59
 * @LastEditors: sueRimn
 * @LastEditTime: 2020-07-24 17:57:26
--> 
# VSCode调试Python

[python调试VSCode官方](https://code.visualstudio.com/docs/python/debugging#_set-configuration-options)
[python调试配置](https://www.cnblogs.com/shine-lee/p/10234378.html)

## 安装扩展

1. 单击`VSCode`左侧菜单栏`Extension`图标，输入`Python`进行搜索，在下方的`Python`扩展程序中点击安装即可。
2. 选择编译器，`Ctrl+Shift+P`，键入`Python: Select Interpreter`，选择相应安装好的`Python`编译器
3. 安装`Linter`,一般来说完成扩展的安装后，会出现提示`Linter pylint is not installed` 的信息，点击安装即可。这个是用来提示错误信息的。

## 运行程序

* F5
* `Terminal`中输入：`python hello.py`或`python3 hello.py`
* 程序页面右键选择在“终端中运行Python文件”

## 调试

配置`launch.json`:
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: 调试",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/src/python_debug_run.py",
            "console": "integratedTerminal"
        }
    ]
}
```
`${workspaceFolder}`为工作空间的根目录。

配置`settings.json`(可不配置有默认路径):
```
{
    "python.pythonPath": "/usr/local/bin/python3"
}
```
`python.pythonPath`为`python`路径，可命令行运行`where python3`查询：
```
/usr/local/bin/python3
/usr/bin/python3
```

`Python`的调试和`C++`基本相同，单击右侧菜单栏中的蜘蛛图标，进入`Debug`。可以在程序行号上单击设置断点，`F11`单步执行，在左侧的`Variable`中观看变量的取值等。

## 问题

### ModuleNotFoundError: No module named '****'

`VS Code` 进行编程`python`时，导入自定义的`Python`包，报错：`No module named '****'`

1. 方案一

如果是`pip3`导入的，可能是默认路径(`/usr/bin/python3`)不对，需要修改为(`/usr/local/bin/python3`)后尝试。
可以添加`.workspace`文件，然后添加`python.pythonPath`。
```
{
	"folders": [
		{
			"path": "."
		}
	],
	"settings": {
		"python.pythonPath": "/usr/local/bin/python3"
	}
}
```
2. 方案二

* 如果在当前文件目录底下可以找到导入的包，那么可以直接使用from ... import ...
* 如果在当前文件目录底下找不到导入的包，则需要向sys.path添加包的所在的绝对位置。
```py
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
```
3. 方案三

[VSCode配置python环境及创建虚拟环境方法](https://www.jianshu.com/p/bbf2ad02841c)