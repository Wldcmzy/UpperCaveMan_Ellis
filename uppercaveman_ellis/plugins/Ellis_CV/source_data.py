import re
import os
import requests
import cv2
import numpy as np
from numpy import ndarray
from nonebot.log import logger
from ..global_args import CV_pic_path, CV_pic_arg
from ..E_tools import form_time_string

CV_n_Iter = 0
def form_pic_name() -> str:
    global CV_n_Iter
    CV_n_Iter = (CV_n_Iter + 1) % 998244353
    return form_time_string() + '_' + str(CV_n_Iter) + '.jpg'

async def resize_by_long_edge(img : ndarray) -> ndarray:
    H, W, D = 1, 1, 1
    new_H, new_W = 50, 50
    if len(img.shape) == 2: H, W = img.shape
    else: H, W, D = img.shape
    if CV_pic_arg['default_long_edge'] > max(H, W): return img
    if H > W:
        multi = CV_pic_arg['default_long_edge'] / H
        new_H, new_W = int(CV_pic_arg['default_long_edge']), int(W * multi)
    else:
        multi = CV_pic_arg['default_long_edge'] / W
        new_H, new_W = int(H * multi), int(CV_pic_arg['default_long_edge'])
    img = cv2.resize(img, (new_W, new_H))
    return img

async def get_1st_pic_url(msg : str) -> str or None:
    '''匹配信息中的第一张图片, 返回连接'''
    pattern = re.compile('\[CQ:image,file=(\w|\d)*\.image,url=https://gchat.qpic.cn/(\w|\d|\/|-|_|\?|=|,)*\]')
    url = pattern.search(msg)
    if url: 
        url = url.group()[ : -2].split('url=')[1]
    return url

async def download_pic(url : str) -> str:
    '''下载图片'''
    if not os.path.exists(CV_pic_path['src']):
        os.makedirs(CV_pic_path['src'])
    res = requests.get(url)
    file_name = form_pic_name()
    file_path = CV_pic_path['src'] + file_name
    with open(file_path, 'wb') as f:
        f.write(res.content)
    return file_name

async def E_flip(file_name : str, axis : int = -1) -> str:
    if not os.path.exists(CV_pic_path['out']):
        os.makedirs(CV_pic_path['out'])
    img = cv2.imread(CV_pic_path['src'] + file_name, 1)
    if img is None: return '暂时改不了动图~'
    img = await resize_by_long_edge(img)
    img = cv2.flip(img, axis)
    cv2.imwrite(CV_pic_path['out'] + file_name, img, [int(cv2.IMWRITE_JPEG_QUALITY), CV_pic_arg['jpg_qulity']])
    return f'[CQ:image,file={CV_pic_path["extra"]}{file_name}]'

async def E_fliphalf(file_name : str, method = 'u') -> str:
    if not os.path.exists(CV_pic_path['out']):
        os.makedirs(CV_pic_path['out'])
    img = cv2.imread(CV_pic_path['src'] + file_name, 1)
    if img is None: return '暂时改不了动图~'
    img = await resize_by_long_edge(img)
    H, W, D = 1, 1, 1
    if len(img.shape) == 2: H, W = img.shape
    else: H, W, D = img.shape
    if method == 'u':
        half = img[ : H // 2 , : ]
        img = np.vstack((half, cv2.flip(half, 0)))
    elif method == 'd':
        half = img[ H // 2 : , : ]
        img = np.vstack((cv2.flip(half, 0), half))
    elif method == 'r':
        half = img[ : , W // 2 : ]
        img = np.hstack((cv2.flip(half, 1), half))
    elif method == 'l':
        half = img[ : , : W // 2 ]
        img = np.hstack((half, cv2.flip(half, 1)))
    cv2.imwrite(CV_pic_path['out'] + file_name, img, [int(cv2.IMWRITE_JPEG_QUALITY), CV_pic_arg['jpg_qulity']])
    return f'[CQ:image,file={CV_pic_path["extra"]}{file_name}]'

async def E_gray(file_name : str) -> str:
    if not os.path.exists(CV_pic_path['out']):
        os.makedirs(CV_pic_path['out'])
    gray = cv2.imread(CV_pic_path['src'] + file_name, 0)
    if gray is None: return '暂时改不了动图~'
    gray = await resize_by_long_edge(gray)
    cv2.imwrite(CV_pic_path['out'] + file_name, gray, [int(cv2.IMWRITE_JPEG_QUALITY), CV_pic_arg['jpg_qulity']])
    return f'[CQ:image,file={CV_pic_path["extra"]}{file_name}]'

async def E_binary(file_name : str, method : int = 1) -> str:
    if method > 5: method = 1
    if not os.path.exists(CV_pic_path['out']):
        os.makedirs(CV_pic_path['out'])
    gray = cv2.imread(CV_pic_path['src'] + file_name, 0)
    if gray is None: return '暂时改不了动图~'
    gray = await resize_by_long_edge(gray)

    thresh = 127
    maxval = 255
    ret, threshed = None, None
    if method == 1:
        #以阈值分割二值化为0和maxval 
        ret, threshed = cv2.threshold(gray,thresh,maxval,cv2.THRESH_BINARY)      
    elif method == 2:
        #以阈值分割二值化为0和maxval
        ret, threshed = cv2.threshold(gray,thresh,maxval,cv2.THRESH_BINARY_INV)  
    elif method == 3:
        #小于阈值变为0
        ret, threshed = cv2.threshold(gray,thresh,maxval,cv2.THRESH_TOZERO)      
    elif method == 4:
        #大于阈值变为0
        ret, threshed = cv2.threshold(gray,thresh,maxval,cv2.THRESH_TOZERO_INV)  
    elif method == 5:
        #大于阈值变为阈值
        ret, threshed = cv2.threshold(gray,thresh,maxval,cv2.THRESH_TRUNC) 

    cv2.imwrite(CV_pic_path['out'] + file_name, threshed, [int(cv2.IMWRITE_JPEG_QUALITY), CV_pic_arg['jpg_qulity']])
    return f'[CQ:image,file={CV_pic_path["extra"]}{file_name}]'


async def E_blur(file_name : str, method : int = 1) -> str:
    if method > 4: method = 1
    if not os.path.exists(CV_pic_path['out']):
        os.makedirs(CV_pic_path['out'])
    img = cv2.imread(CV_pic_path['src'] + file_name, 1)
    if img is None: return '暂时改不了动图~'
    img = await resize_by_long_edge(img)
    if method == 1:
        #均值滤波
        img = cv2.blur(img, (9 ,9))
    elif method == 2:
        #方框滤波 当normallize为True时等同于均值滤波
        img = cv2.boxFilter(img, -1, (9, 9), normalize = False)
    elif method == 3:
        #高斯滤波
        img = cv2.GaussianBlur(img, (9, 9), sigmaX = 97)
    elif method == 4:
        #中值滤波
        img = cv2.medianBlur(img, 9)

    cv2.imwrite(CV_pic_path['out'] + file_name, img, [int(cv2.IMWRITE_JPEG_QUALITY), CV_pic_arg['jpg_qulity']])
    return f'[CQ:image,file={CV_pic_path["extra"]}{file_name}]'


async def E_canny(file_name : str) -> str:
    if not os.path.exists(CV_pic_path['out']):
        os.makedirs(CV_pic_path['out'])
    img = cv2.imread(CV_pic_path['src'] + file_name, 0)
    if img is None: return '暂时改不了动图~'
    img = await resize_by_long_edge(img)
    img = cv2.Canny(img, 80, 130)
    cv2.imwrite(CV_pic_path['out'] + file_name, img, [int(cv2.IMWRITE_JPEG_QUALITY), CV_pic_arg['jpg_qulity']])
    return f'[CQ:image,file={CV_pic_path["extra"]}{file_name}]'
