#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project: Weibo Spider
@File: GetConfig.py
@Author: RyanZhang
@Date: 2022-10-08
"""

import json
import os


# type : pc & mobile
def getCookie(type):
    runPath = os.getcwd()
    info = json.load(open(runPath + "/cookie.json", encoding="utf-8"))
    for item in info:
        return item.get(type)
