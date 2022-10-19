#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project: Weibo Spider
@File: Detail.py
@Author: RyanZhang
@Date: 2022-10-08
"""
import datetime

from bs4 import BeautifulSoup
import requests
import json
import Clean
import ConvertTime


def getArt(mid, cookie):
    print("Parsing: {}".format(mid))
    url = "https://m.weibo.cn/status/{}".format(mid)
    head = {
        "User-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": cookie
    }
    session = requests.Session()
    res = session.get(url, headers=head, timeout=10)
    soup = BeautifulSoup(res.text, 'html.parser')
    script = soup.find_all('script')[2].text
    temps = script.split("var $render_data = [")[1].split("][0] || {};")[0]
    jsonData = json.loads(temps)
    # Data Split
    userName = jsonData.get("status").get("user").get("screen_name")
    verified = jsonData.get("status").get("user").get("verified")
    verifiedType = jsonData.get("status").get("user").get("verified_type")
    verifiedReason = jsonData.get("status").get("user").get("verified_reason")
    createTime = ConvertTime.convert(jsonData.get("status").get("created_at"))
    content = Clean.cleanAll(jsonData.get("status").get("text"))
    picList = jsonData.get("status").get("pic_ids")
    # result list
    result = [mid, userName, verified, verifiedType, verifiedReason, createTime, content, picList]
    return result


