#! /usr/bin/env python
# coding=utf-8
# -*- coding:utf8 -*-

import subprocess
import shutil
import os
import time
import sys
from PIL import Image


def CutLeftHalf(imagePath,targetPath):
	#打开图像文件
	image = Image.open(imagePath)
	width, height = image.size
	# 计算左侧一半的宽度
	half_width = width // 2
	left_half = image.crop((0, 0, half_width, height))
	newImagePath = ''
	#如果没有传入目标路径 则自动根据图片
	if not targetPath:
		#获得图片的路径不包含后缀，图片的后缀
		imagePathWithoutExten,imageExten = os.path.splitext(imagePath)
		newImagePath = imagePathWithoutExten + '_half_left' + imageExten
	else :
		newImagePath = targetPath

	left_half.save(newImagePath)
	image.close()

def CutBottomHalf(imagePath,targetPath):
	#打开图像文件
	image = Image.open(imagePath)
	width, height = image.size
	# 计算下半部分高度
	half_height = height // 2
	left_bottom = image.crop((0, half_height, width, height))
	newImagePath = ''
	#如果没有传入目标路径 则自动根据图片
	if not targetPath:
		#获得图片的路径不包含后缀，图片的后缀
		imagePathWithoutExten,imageExten = os.path.splitext(imagePath)
		newImagePath = imagePathWithoutExten + '_half_bottom' + imageExten
	else :
		newImagePath = targetPath

	left_bottom.save(newImagePath)
	image.close()

def CutQuarter(imagePath,targetPath):
	#打开图像文件
	image = Image.open(imagePath)
	width, height = image.size
	# 计算左下角1/4的宽度和高度
	quarter_width = width // 2
	quarter_height = height // 2
	left_bottom_quarter = image.crop((0, height - quarter_height, quarter_width, height))
	newImagePath = ''
	#如果没有传入目标路径 则自动根据图片
	if not targetPath:
		#获得图片的路径不包含后缀，图片的后缀
		imagePathWithoutExten,imageExten = os.path.splitext(imagePath)
		newImagePath = imagePathWithoutExten + '_quarter' + imageExten
	else :
		newImagePath = targetPath

	left_bottom_quarter.save(newImagePath)
	image.close()

print("打印参数内容")
for x in sys.argv:
	print(x)
print("打印结束！！！")
_imagePath=''
_targetPath=''
_cutType =  '0' # 1需要CutLeftHalf  2需要 CutBottomHalf  3需要CutQuarter

# 获取命令行参数长度 去掉默认的一个参数
argvLenth=len(sys.argv) - 1
if  argvLenth < 2:
	print("当前参数个数 : " + str(argvLenth) +" 请提供至少2个参数：_imagePath ，_cutType")
else:
	_imagePath = sys.argv[1]
	_cutType = sys.argv[2]
	if len(sys.argv) > 3:
		_targetPath = sys.argv[3]

print("_imagePath : " + _imagePath)
print("_targetPath : " + _targetPath)
print("_cutType : " + _cutType)

if _cutType == '1':
	CutLeftHalf(_imagePath,_targetPath)
elif _cutType == '2':
	CutBottomHalf(_imagePath,_targetPath)
elif _cutType == '3':
	CutQuarter(_imagePath,_targetPath)
else:
	print("没有类型参数！！！")




