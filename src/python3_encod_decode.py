#!/usr/bin/python3
#coding=utf-8

#url编码
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

url = 'https://maimai.cn/sdk/search/get?query=成都'

encode_url = url_encode(url)
print(encode_url)

decode_url = url_decode(encode_url)
print(decode_url)