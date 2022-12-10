#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project: Weibo Spider
@File: Video2Img.py
@Author: RyanZhang
@Date: 2022-11-14
"""

import cv2
import os

def v2i(path):
    cap = cv2.VideoCapture(os.path.join(path, "video.mp4"))
    # video fps
    fps = cap.get(cv2.CAP_PROP_FPS)
    # video frames
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    index = 0
    fps_list = []
    while cv2.waitKey(0):
        retval, image = cap.read()
        index += 1
        # print(f"fps:{index}")
        if index == int(frames) or index == 1:
            prefix = str(index).zfill(8) + ".png"
            cv2.imwrite(os.path.join(path, prefix), image)
            fps_list.append(index)
        elif index < int(frames):
            if index % int(fps) == 0:
                prefix = str(index).zfill(8) + ".png"
                cv2.imwrite(os.path.join(path, prefix), image)
                fps_list.append(index)
        elif index > frames:
            break
    return fps_list

