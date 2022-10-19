#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project: Weibo Spider
@File: index.py
@Author: RyanZhang
@Date: 2022-10-08
"""

import requests
import GetConfig
import Detail
import SaveFile
from bs4 import BeautifulSoup

pc_cookie = ""
mobile_cookie = ""

# Get the function of the page blog
def getMids(keyword, pageNum):
    # Prompt
    print("Working--keyword: {} --page: {}".format(keyword,pageNum))
    # Construct request address
    url = "https://s.weibo.com/weibo?q={}&page={}".format(keyword, pageNum)
    # Request data message header
    head = {
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": pc_cookie
    }
    # Initiate a Get request
    htmlData = requests.get(url, headers=head).text
    # Create a list to store posts ID
    mids = []
    # Load bs4 lib
    soup = BeautifulSoup(htmlData, features="html.parser")
    # Find DIV
    div = soup.findAll("div", attrs={"action-type": "feed_list_item"})
    # Get posts MID (similar to UUID)
    for i in div:
        mid = i.get("mid")
        mids.append(mid)
    return mids


# This Test Code Need to delete

if __name__ == '__main__':
    # Get the PC side Cookie
    print("Please Input Search keyword")
    keyword = input()
    num = -1
    while num < 1:
        print("Please Input Search Page Number >=1")
        num = eval(input())
    pc_cookie = GetConfig.getCookie("pc")
    mobile_cookie = GetConfig.getCookie("mobile")
    detail = []
    for i in range(1, num + 1):
        for j in getMids(keyword, i):
            try:
                tmp = Detail.getArt(j, mobile_cookie)
            except:
                print("Error, Could be a page overflow.")
                pass
            # Prevent repetition
            try:
                if tmp not in detail:
                    # Judge whether you have a picture or not
                    if tmp[7]:
                        folder = SaveFile.Folder(tmp)
                        tmp.append(folder)
                    else:
                        tmp.append('')
                    detail.append(tmp)
            except:
                print("Error, Maybe the folder already exists")
    SaveFile.CSV(detail)
