#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project: Weibo Spider
@File: SaveFile.py
@Author: RyanZhang
@Date: 2022-10-08
"""
import datetime
import os
import requests
import urllib


# 建立存储图片的文件夹
def Folder(mid):
    # 今日日期
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    # 相对路径
    relativePath = f"{today}/{mid}"
    # 绝对路径
    folderPath = os.path.join(os.getcwd(), relativePath)
    print(folderPath)
    # 判断文件夹是否存在
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    return relativePath

# 下载图片
def downloadImage(path, list):
    for i in list:
        IMAGE_URL = "https://wx3.sinaimg.cn/large/{}.jpg".format(i)
        r = requests.get(IMAGE_URL)
        with open(os.path.join(path, '{}.png'.format(i)), 'wb') as f:
            f.write(r.content)

def downloadVideo(path, url):
    urllib.request.urlretrieve(url, os.path.join(path, "video.mp4"))

# CSV写入方法已废弃
# 数据写入已于2022年11月17日转移至WriteSql，通过MySQL数据库存储数据，保证数据可用性
# Data saving CSV
# def CSV(data):
#     # Get Now datetime
#     now = datetime.datetime.today().strftime("%Y_%m_%d_%H_%M")
#     # 2022-10-19 Update List
#     csvTitle = ['mid', 'userName', 'verified', 'verifiedType', 'verifiedReason', 'createTime', 'content', 'picList', 'path']
#     path = os.getcwd() + "/" + now + ".csv"
#     # No newline will result in blank lines
#     with open(path, mode="w", encoding="utf-8-sig", newline="") as f:
#         # Create an instance of csv.writer based on an open file
#         write = csv.writer(f)
#         # Write csv Title (First row) only write one row
#         write.writerow(csvTitle)
#         # Write csv Data (every row)
#         write.writerows(data)
#     print("Finish the work，CSV File Path: {}".format(path))


