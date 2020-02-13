# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-01-24 10:15:51
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-01-25 16:37:54

from PIL import Image, ImageDraw
from random import uniform, random
from extrapol import *
import time

width = 900
height = 500

Black = (0, 0, 0, 255)


def createAPic():
	image = Image.new('RGBA', (width, height), Black)
	return image

def show_save(pict, pictName, formt):
	fileName = pictName + '.' + formt
	pict.show()
	pict.save(fileName, formt)

def extrapolTheLine(line, size):
	xa = 0
	xb = 1
	# print(" extrapolTheLine size", size)
	# print("line : ", line)
	try:
		while xb+1 < len(line):
			# print("xb : ", xb, "line :  ", line[xb])
			while line[xb] == 0:
				xb +=1
			i = xa+1
			while i < xb:
				#line[i] = int(extrapol(i, xa, line[xa], xb, line[xb]))
				line[i] = (int(uniform(1, 255)))
				i += 1
			xa = xb
			xb = xa + 1
	except IndexError:
		print("ERREUR !")
		print("line : ", line)
		print("size de la ligne : ", len(line))
		time.sleep(1000)
	return line

def fusionLine(line):
	level = len(line)
	mlSize = len(line[0])
	newLine = []
	for i in range (0, mlSize):
		res = 0
		for j in range (0, level):
			res += line[j][i]
		newLine.append(int(res/level))
	return newLine

def	createList(size):
	lstgen = []
	temp = []
	level = size-1
	for i in range(0, (size+1)):
		temp.append(int(uniform(1, 255)))
	lstgen.append(temp)
	temp = []
	while level > 0:
		if size%level == 0:
			temp = [0] * (size+1)
			c = 0
			while c <= size:
				temp[c] = int(uniform(1, 255))
				c += int(size/level)
			#temp = extrapolTheLine(temp, size)
			lstgen.append(temp)
		level -= 1
	final_line = fusionLine(lstgen)
	return final_line

res = []
for i in range (0, height):
	res.append(createList(width))

# for i in res:
# 	print(i)

def myDrawPerlinTestOne(pict, lst):
	draw = ImageDraw.Draw(pict)
	for j in range (0, height):
		for i in range (0, width):
			tPXL = (lst[j][i],lst[j][i],lst[j][i])
			draw.point((i, j), fill=tPXL)

img = createAPic()
myDrawPerlinTestOne(img, res)
show_save(img, "toto", "png")