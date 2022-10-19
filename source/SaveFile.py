#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project: Weibo Spider
@File: SaveFile.py
@Author: RyanZhang
@Date: 2022-10-08
"""
import csv
import datetime
import os
import requests


# Create a folder to store pictures
def Folder(data):
    folderPath = os.getcwd() + "/Spider/{}_{}".format(data[1], data[0])
    os.makedirs(folderPath)
    if data[7]:
        downloadImage(folderPath, data[7])
    return folderPath

# Data saving CSV
def CSV(data):
    # Get Now datetime
    now = datetime.datetime.today().strftime("%Y_%m_%d_%H_%M")
    # 2022-10-19 Update List
    csvTitle = ['mid', 'userName', 'verified', 'verifiedType', 'verifiedReason', 'createTime', 'content', 'picList', 'path']
    path = os.getcwd() + "/" + now + ".csv"
    # No newline will result in blank lines
    with open(path, mode="w", encoding="utf-8-sig", newline="") as f:
        # Create an instance of csv.writer based on an open file
        write = csv.writer(f)
        # Write csv Title (First row) only write one row
        write.writerow(csvTitle)
        # Write csv Data (every row)
        write.writerows(data)
    print("Finish the work，CSV File Path: {}".format(path))


# Weibo Image Download
def downloadImage(path, list):
    for i in list:
        IMAGE_URL = "https://wx3.sinaimg.cn/large/{}.jpg".format(i)
        r = requests.get(IMAGE_URL)
        with open(path + '/{}.jpg'.format(i), 'wb') as f:
            f.write(r.content)
