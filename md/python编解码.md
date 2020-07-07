<!-- TOC -->

- [python编解码](#python编解码)
    - [url编解码](#url编解码)

<!-- /TOC -->

# python编解码

## url编解码

python：
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
[python编码](https://github.com/matiastang/python-story/blob/master/src/python_encod_decode.py)

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
[python3编码](https://github.com/matiastang/python-story/blob/master/src/python3_encod_decode.py)