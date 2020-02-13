# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2020-01-23 17:14:51
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-02-13 13:48:16

# Cela fait un moment que je voulais refaire ce sous projet du RT ... (22/01/2020)
# ba voici au moins une nouvelle fonctione d'extrapolation ^^ (recupéré sur wikipédia)

#

def extrapolPlus(x, xa, ya, xb, yb):
	numrtOne = ya-yb
	den = xa-xb
	numrtTwo = (xa*yb)-(xb*ya)
	ybis = numrtOne/den
	ybis *= x
	temp = numrtTwo/den
	ybis += temp
	print("y bis", ybis)
	y = (((ya-yb)/(xa-xb))*x)+(((xa*yb)-(xb*ya))/(xa-xb))
	print("y = ", y)
	return y

def extrapol(x, xa, ya, xb, yb, printRes=False):
	y = (((ya-yb)/(xa-xb))*x)+(((xa*yb)-(xb*ya))/(xa-xb))
	if printRes:
		print("y = ", y)
	return y