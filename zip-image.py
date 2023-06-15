#coding=utf-8

import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 当前目录读取一张图片（499Kb，1920*1080）
img = cv.imread('hintersee01.jpg')

# 压缩图片（226Kb）
cv.imwrite('temp/compress1.jpg', img, [cv.IMWRITE_JPEG_QUALITY, 50])

# 调整长宽（长宽指定数值，非等比例缩放时图片会变形）
img2 = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imwrite('temp/resize2.jpg', img2)

# 调整长宽（长宽各调整为原来的一半，即 0.5）
img3 = cv.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
cv.imwrite('temp/resize3.jpg', img3)
