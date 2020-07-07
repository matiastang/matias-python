<!-- TOC -->

- [python编解码](#python编解码)
    - [url编解码](#url编解码)

<!-- /TOC -->

# python编解码

## url编解码

python：
字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码， 即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
* decode的作用是将其他编码的字符串转换成unicode编码
* encode的作用是将unicode编码转换成其他编码的字符串
```py
#coding=utf-8

import urllib

def url_encode(url):
    """
    url编码
    :param url: 需要编码的url(gbk)
    :return: url编码后数据
    """
    #如果此网站编码是gbk的话，需要进行解码，从gbk解码成unicode，再从Unicode编码编码为utf-8格式。
    url = url.decode('gbk', 'replace')
    return urllib.quote(url.encode('utf-8', 'replace'))

def url_decode(url):
    """
    url解码
    :param url: 需要解码的url
    :return: url解码后数据
    """
    return urllib.unquote(url).decode('utf-8', 'replace').encode('gbk', 'replace')
```
[python编解码](https://github.com/matiastang/python-story/blob/master/src/python_encod_decode.py)

python3：
```py
from urllib import parse

def url_encode(url: str):
    """
    url编码
    :param url: 需要编码的url(gbk)
    :return: url编码后数据
    """
    return parse.quote(url)

def url_decode(url: str):
    """
    url解码
    :param url: 需要解码的url
    :return: url解码后数据
    """
    return parse.unquote(url)
```
[python3编解码](https://github.com/matiastang/python-story/blob/master/src/python3_encod_decode.py)