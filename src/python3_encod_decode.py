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

test_encode_url = 'https://open.taou.com/maimai/gossip/v3/get?version=5.2.74&ver_code=android_20274&channel=MyAPP&vc=Android%207.1.2%2F25&push_permit=1&net=no&open=icon&appid=3&device=Google%20Pixel&imei=352531085288684&udid=df35400d-c7a5-47b3-9763-bacab12611d8&is_push_open=1&isEmulator=0&rn_version=0.59.10&sm_did=Duk4NXGURJ/NwPOqUVwx2ZiqPnuJeGucVagwtblZwzfHE7jrdUXOip3uyP8N8o31hkE9OIRQ23sJJsToti5zRNrA&u=231080635&access_token=1.f3bff6e5dfae10fb8673ba3c30df8ca4&real_imei=352531085288684&webviewUserAgent=Mozilla%2F5.0%20(Linux%3B%20Android%207.1.2%3B%20Pixel%20Build%2FNJH47F%3B%20wv)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Version%2F4.0%20Chrome%2F55.0.2883.91%20Mobile%20Safari%2F537.36&density=2.625&screen_width=1080&screen_height=1794&launch_uuid=e2338ff0-ddbe-420c-9db5-63fe3ffa8a52&session_uuid=3f9a4963-4eca-464d-95dd-915a3b3cfb76&last_launch_time=1594260688411&egid=ac985362a8c011ea89d3801844e50190&gid=26386352'
test_decode_url = url_decode(test_encode_url)
print(test_decode_url)