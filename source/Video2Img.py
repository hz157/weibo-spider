#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project: Weibo Spider
@File: Video2Img.py
@Author: RyanZhang
@Date: 2022-11-14
"""

import cv2
import numpy
import os


def v2i(path=os.path.join(os.getcwd(), "video")):
    files_list = os.listdir(path)
    for file in files_list:
        cap = cv2.VideoCapture(os.path.join(os.getcwd(), 'video', file))
        # 帧率(fps)
        fps = cap.get(cv2.CAP_PROP_FPS)
        # 总帧数(frames)
        frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        # 生成文件夹
        if not os.path.exists(file):
            os.makedirs(file)
        index = 0
        while cv2.waitKey(0):
            retval, image = cap.read()
            index += 1
            # print(f"fps:{index}")
            if index == int(frames) or index == 1:
                prefix = str(index).zfill(5) + ".png"
                cv2.imwrite(os.path.join(file, prefix), image)
            elif index < int(frames):
                if index % int(fps) == 0:
                    prefix = str(index).zfill(5) + ".png"
                    cv2.imwrite(os.path.join(file, prefix), image)
                    # cv2.imshow("video",image)
            elif index > frames:
                break

