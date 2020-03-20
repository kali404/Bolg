#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 下午11:35
# @Author  : Aries
# @File    : image_to_qiniu.py
# @Software: PyCharm
# @Email   : dewujie64@gmail.com
import re
from django.conf import settings
from qiniu import Auth, put_file, etag
from qiniu import BucketManager
import qiniu.config
import requests
import json

import time
import os


# 七牛的配置信息

def markdown_to_img(text):
    # 把传过来的markdown 中的图片找出来
    img_list = re.findall(r'!\[.*?\]\((.*?)\)', text)  # img_list :['static/images/editor/xxx.png',]
    for img_path in img_list:
        print(img_path)
        if 'http:' in img_path:
            break
        img_name = img_path.split('/')[-1]
        img_path_all = settings.BASE_DIR + img_path
        qiniu_img = upload(img_name, img_path_all)
        print(qiniu_img)
        text = re.sub('\({}\)'.format(img_path), '(' + qiniu_img + ')', text)
    return text


def img_to_qiniu(img_name):
    if 'http://' in img_name:
        return img_name
    img_path = settings.BASE_DIR + settings.MEDIA_URL + img_name
    img_url = upload(img_name, img_path)
    return img_url


def upload(key, localfile):
    access_key = ''
    secret_key = ''
    bucket_name = ''
    q = Auth(access_key, secret_key)

    buc = BucketManager(q)
    res, info1 = buc.stat(bucket_name, key)
    if (res != None):
        return 'http://q70q0va20.bkt.clouddn.com/' + key

    print(localfile)
    if (os.path.exists(localfile) == False):
        exit('文件不存在')
    # 获取上传的token
    token = q.upload_token(bucket_name, key, 3600)

    ret, info = put_file(token, key, localfile)
    html = 'http://q70q0va20.bkt.clouddn.com/{}'.format(ret.get('key'))
    return html


if __name__ == '__main__':
    markdown_to_img('''![](img\bubble.png)
    ![](img\6ntmilf81j.gif)

    ```python
    def bubble_sort(tlist):
        n = len(tlist)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if tlist[j] > tlist[j + 1]:
                    tlist[j], tlist[j + 1] = tlist[j + 1], tlist[j]
            print(tlist)
    ```
    
    ### 2. 选择排序（O(n<sup>2</sup>）)
    
    ![](img\selected.jpg)''')
