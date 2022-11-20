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
import Sql
import jieba
import threading
from bs4 import BeautifulSoup

pc_cookie = ""
mobile_cookie = ""
allPage = 2


# Get the function of the page blog
def getMids(keyword, pageNum=1):
    global allPage
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
    if pageNum == 1:
        page = str(soup.findAll("ul", attrs={"action-type": "feed_list_page_morelist"})).split('\n')
        allPage = len(page) - 2
    # Get posts MID (similar to UUID)
    for i in div:
        mid = i.get("mid")
        mids.append(mid)
    return mids

extentWord = {}

def main(keyword):
    global pc_cookie, mobile_cookie
    pc_cookie = GetConfig.getCookie("pc")
    mobile_cookie = GetConfig.getCookie("mobile")
    curr = 1
    while curr < allPage:
        mids = getMids(keyword, curr)
        if curr == 1:
            print(f"Keyword: {keyword}, Total Page Number: {allPage} Press any key to continue\n")
        print("Working--keyword: {} --page: {}".format(keyword, curr))
        for j in mids:
            # Prevent repetition
            try:
                tmp = Detail.getArt(j, mobile_cookie)
                if not Sql.verifMid(tmp[0]):
                    if tmp[7]:
                        # 创建文件夹
                        folder = SaveFile.Folder(tmp)
                        tmp.append(folder)
                    else:
                        tmp.append('')
                    Sql.writeData(tmp, keyword)
            except:
                print("Error, Maybe the folder already exists")
        curr = curr + 1



if __name__ == '__main__':
    # Get the PC side Cookie
    print("Please Input Search keyword")
    keyword = input()
    main(keyword)

