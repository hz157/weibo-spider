#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project: Weibo Spider
@File: Clean.py
@Author: RyanZhang
@Date: 2022-10-18
"""

import re


# 清理微博话题
def cleanTopic(data):
    try:
        start = data.index('#')
        end = data[start + 1:len(data)].index('#') + start
        remove = data[start:end + 2]
        data = data.replace(remove, '')
        return cleanTopic(data)
    except:
        return data


# 清理ZWSP 空格
def replace(data):
    result = data.replace('ZWSP', '').replace('<br />', ' ').replace('<br>', ' ')
    return result


# 清理At用户选项
def cleanAt(data):
    try:
        start = data.index('@')
        end = data[start + 1:len(data)].index(' ') + start
        remove = data[start:end + 2]
        data = data.replace(remove, '')
        return cleanTopic(data)
    except:
        return data


# 清理Emoji表情
def cleanEmoji(data):
    # Filter facial expressions
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub('', data)


# 清理<a>HTML标签
def cleanALabel(data):
    try:
        start = data.index('<a')
        end = data[start + 1:len(data)].index('</a>') + start
        remove = data[start:end + 5]
        data = data.replace(remove, '')
        return cleanALabel(data)
    except:
        return data


# 清理<Span>HTML标签
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

