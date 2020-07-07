#coding=utf-8

#url编码
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

url = 'https://maimai.cn/sdk/search/get?query=成都'

encode_url = url_encode(url)
print(encode_url)

decode_url = url_decode(encode_url)
print(decode_url)