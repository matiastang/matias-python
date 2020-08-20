# python生成requirements.txt

## 生成

有两种方式生成`requirements.txt`文件。

1. 适用于 单虚拟环境的情况：

```
pip freeze > requirements.txt
```
只适用于单虚拟环境？因为这种方式，会将环境中的依赖包全都加入，如果使用的全局环境，则下载的所有包都会在里面，不管是不时当前项目依赖的

2. 使用 pipreqs
[github地址](https://github.com/bndr/pipreqs)
```
# 安装
pip install pipreqs
# 在当前目录生成
pipreqs . --encoding=utf8 --force
```
注意 `--encoding=utf8` 为使用`utf8`编码，不然可能会报`UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 406: illegal multibyte sequence` 的错误。
`--force` 强制执行，当 生成目录下的`requirements.`txt存在时覆盖。`

## 使用

`requirements.txt`安装依赖的方式：
```
pip install -r requirements.txt
```