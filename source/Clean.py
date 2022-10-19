#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project: Weibo Spider
@File: Clean.py
@Author: RyanZhang
@Date: 2022-10-18
"""

import re


def cleanTopic(data):
    try:
        start = data.index('#')
        end = data[start + 1:len(data)].index('#') + start
        remove = data[start:end + 2]
        data = data.replace(remove, '')
        return cleanTopic(data)
    except:
        return data


def replace(data):
    result = data.replace('ZWSP', '').replace('<br />', ' ').replace('<br>', ' ')
    return result


def cleanAt(data):
    try:
        start = data.index('@')
        end = data[start + 1:len(data)].index(' ') + start
        remove = data[start:end + 2]
        data = data.replace(remove, '')
        return cleanTopic(data)
    except:
        return data


# def cleanEmoji(data):
#     # Filter characters other than Chinese, English and numbers
#     res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z^0-9]")
#     return res.sub('', data)


def cleanEmoji(data):
    # Filter facial expressions
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub('', data)


def cleanALabel(data):
    try:
        start = data.index('<a')
        end = data[start + 1:len(data)].index('</a>') + start
        remove = data[start:end + 5]
        data = data.replace(remove, '')
        return cleanALabel(data)
    except:
        return data


def cleanSpanLabel(data):
    try:
        start = data.index('<span')
        end = data[start + 1:len(data)].index('</span>') + start
        remove = data[start:end + 8]
        data = data.replace(remove, '')
        return cleanSpanLabel(data)
    except:
        return data



def cleanBracket(data):
    try:
        start = data.index('【')
        end = data[start + 1:len(data)].index('】') + start
        remove = data[start:end + 2]
        data = data.replace(remove, '')
        return cleanSpanLabel(data)
    except:
        return data


def cleanLabel(data):
    return cleanSpanLabel(cleanALabel(data))


def cleanAll(data):
    return cleanTopic(replace(cleanAt(cleanEmoji(cleanBracket(cleanLabel(data))))))

