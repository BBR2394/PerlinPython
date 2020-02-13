# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-01-23 16:13:37
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-02-13 10:38:59

#! /bin/python3

from PIL import Image, ImageDraw
from random import uniform, random
from extrapol import *

width = 512
height = 512

Black = (0, 0, 0, 255)

def createAPic():
	image = Image.new('RGBA', (width, height), Black)
	return image

def show_save(pict, pictName, formt):
	fileName = pictName + '.' + formt
	pict.show()
	pict.save(fileName, formt)

def drawOnPict(pict):
	draw = ImageDraw.Draw(pict)
	GREEN = (0, 255, 0, 0)
	draw.line((0, height//2,
	          width, height//2),
	          fill=GREEN)
	draw.line((width//2, 0,
	          width//2, height),
	          fill=GREEN)
	
	BLUE = (0, 0, 255, 0)
	draw.ellipse((width//4, height//4,
	             3*width//4, 3*height//4),
	             outline=BLUE)
	
	BLACK = (0, 0, 0, 0)
	draw.text((20, 20), "Cercle trigonométrique", fill=BLACK)

def myDraw(pict):
	draw = ImageDraw.Draw(pict)
	sens = True
	PXL = 0
	for j in range (0, height):
		for i in range (0, width):
			tPXL = (PXL,PXL,PXL)
			if sens:
				draw.point((i, j), fill=tPXL)
				PXL += 1
				if PXL > 255:
					sens = False
					PXL = 254
			else:
				draw.point((i, j), fill=tPXL)
				PXL -= 1
				if PXL < 0:
					sens = True
					PXL = 1
		PXL = 0
		sens = True

#uniform c'est la fonction de generateur de nombre aleatoire
def myDrawRand(pict):
	draw = ImageDraw.Draw(pict)
	PXL = int(uniform(0, 255))
	for j in range (0, height):
		for i in range (0, width):
			tPXL = (PXL,PXL,PXL)
			draw.point((i, j), fill=tPXL)
			PXL = int(uniform(0, 255))

def createTwoLayer():
	line = []
	lstOne = []
	lstTwo = []
	for j in range (0, 10):
		for i in range (0, 10):
			line.append(int(uniform(0, 255)))
		lstOne.append(line)
		line = []
	for j in range (0, 6):
		for i in range (0, 6):
			line.append(int(uniform(0, 255)))
		lstTwo.append(line)
		line = []
	print(lstOne)
	print(lstTwo)


def drawTheDoubleTab(tab, pict):
	draw = ImageDraw.Draw(pict)
	for j in range (0, height):
		for i in range (0, width):
			tPXL = (tab[j][i],tab[j][i],tab[j][i])
			draw.point((i, j), fill=tPXL)

def firstLayerTotalRand():
	tab = [[]]
	for j in range (0, height):
		for i in range (0, width):
			aPXL = int(uniform(0, 255))
			tab[j].append(aPXL)
		#print("a line of pxl : ", tab[j])
		tab.append([])
	print("infirst layer total rand : ", tab)
	return tab

#quand j'extrapole entre deux point separé de 5 pixel
def layerFive():
	print("->dans layer five")
	tab = []
	aPXL = int(uniform(0, 255))
	tab.append(aPXL)
	for i in range (1, int(width/5)):
		aPXL = int(uniform(0, 255))
		tab.append(aPXL)
	print("a line of pxl : ", tab[j])
	tab.append([])
		
	print("infirst layer total rand : ", tab)
	return tab


def main():
	print("here is where the magic happen")
	img = createAPic()
	#drawOnPict(img)
	tabOne = firstLayerTotalRand()
	layerFive()
	drawTheDoubleTab(tabOne, img)
	

	#lstTwo = createTwoLayer()
	#myDraw(img)
	#myDrawRand(img)
	show_save(img, "toto", "png")

main()