# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-02-13 10:37:16
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-02-13 13:51:14

from PIL import Image, ImageDraw

from random import uniform, random
from extrapol import *

width = 1000
height = 1000

Black = (0, 0, 0, 255)

coef = 10

def createAPic():
	image = Image.new('RGBA', (width, height), Black)
	return image

def show_save(pict, pictName, formt):
	fileName = pictName + '.' + formt
	pict.show()
	pict.save(fileName, formt)

def myDraw(pict, tab):
	draw = ImageDraw.Draw(pict)
	PXL = int(uniform(0, 255))
	for j in range (0, height):
		for i in range (0, width):
			PXL = tab[j][i]
			tPXL = (PXL,PXL,PXL)
			draw.point((i, j), fill=tPXL)

def extrapolLine(tab, indexLine):
	i = 0
	while i < len(tab[indexLine])-1:
		#print("i au debut : ", i)
		#print(" i = ", i, "; ya = ", tab[indexLine][i], "; yb = ", tab[indexLine][i+1])
		for c in range(1, coef):
			ya = tab[indexLine][i]
			yb = tab[indexLine][i+c]
			res = extrapol(c, 0, ya, coef, yb)
			#print("resultat intermediaire pour c = ", c, "qui donne res = ", res)
			tab[indexLine].insert(c+i, int(res))
		i += coef
	#print("a la fin : ", tab[indexLine])


def createIntermediateLine(tab):
	subLine = []
	for i in range(0, int(width/coef)+1):
		subLine.append(0)
	j = 1
	while j < height:
		#print("j = ", j)
		tab.insert(j, subLine[:])
		j += 1
		if j % coef == 0:
			j += 1

def extrapolColumn(tab, indexCol):
	line = 0
	i = 0
	while i < height:
		for c in range(1, coef):
			ya = tab[i][indexCol]
			yb = tab[i+coef][indexCol]
			res = extrapol(c, 0, ya, coef, yb)
			#print("resultat intermediaire pour c = ", c, "qui donne res = ", res)
			tab[c+i][indexCol] = int(res)
		i += coef


def layerFive():
	#print("->dans layer five")
	yTab = []
	for j in range(0, int((height/coef)+1)):
		tab = []
		aPXL = int(uniform(0, 255))
		tab.append(aPXL)
		for i in range (1, int((width/coef)+1)):
			aPXL = int(uniform(0, 255))
			tab.append(aPXL)
		##print("a line of pxl : ", tab)
		yTab.append(tab)

	for c in range(0, len(yTab)):
		print("->ligne : ", c, " : ", yTab[c])
	#print("taille d'une ligne : ", len(yTab[1]))
	return yTab

generalTab = layerFive()
for c in range(0, len(generalTab)):
	print("->ligne : ", c, " : ", generalTab[c])
print("--------------------------------")
createIntermediateLine(generalTab)
for c in range(0, len(generalTab)):
	print("->ligne : ", c, " : ", generalTab[c])

for c in range(0, len(generalTab)):
	print("->ligne : ", c, " : ", generalTab[c])

for col in range(0, int(width/coef)):
	extrapolColumn(generalTab, col)
for c in range(0, len(generalTab)):
	print("->ligne : ", c, " : ", generalTab[c])
for i in range(len(generalTab)):
	extrapolLine(generalTab, i)
print("--------------------------------")
for c in range(0, len(generalTab)):
	print("->ligne : ", c, " : ", generalTab[c])

coef = 10
generalTab2 = layerFive()
for c in range(0, len(generalTab2)):
	print("->ligne : ", c, " : ", generalTab2[c])
print("--------------------------------")
createIntermediateLine(generalTab2)
for c in range(0, len(generalTab2)):
	print("->ligne : ", c, " : ", generalTab2[c])

for c in range(0, len(generalTab2)):
	print("->ligne : ", c, " : ", generalTab2[c])

for col in range(0, int(width/coef)):
	extrapolColumn(generalTab2, col)
for c in range(0, len(generalTab2)):
	print("->ligne : ", c, " : ", generalTab2[c])
for i in range(len(generalTab2)):
	extrapolLine(generalTab2, i)
print("--------------------------------")
for c in range(0, len(generalTab2)):
	print("->ligne : ", c, " : ", generalTab2[c])

coef = 20
generalTab3 = layerFive()
for c in range(0, len(generalTab3)):
	print("->ligne : ", c, " : ", generalTab3[c])
print("--------------------------------")
createIntermediateLine(generalTab3)
for c in range(0, len(generalTab3)):
	print("->ligne : ", c, " : ", generalTab3[c])

for c in range(0, len(generalTab3)):
	print("->ligne : ", c, " : ", generalTab3[c])

for col in range(0, int(width/coef)):
	extrapolColumn(generalTab3, col)
for c in range(0, len(generalTab3)):
	print("->ligne : ", c, " : ", generalTab3[c])
for i in range(len(generalTab3)):
	extrapolLine(generalTab3, i)
print("--------------------------------")
for c in range(0, len(generalTab3)):
	print("->ligne : ", c, " : ", generalTab3[c])


finalTab = generalTab[:]

for j in range(0, height):
	for i in range(0, width):
		finalTab[j][i] =  int((generalTab[j][i] + generalTab2[j][i] + generalTab3[j][i] + int(uniform(0, 255))) / 4)

img = createAPic()
myDraw(img, finalTab)
show_save(img, "toto", "png")

print(finalTab)