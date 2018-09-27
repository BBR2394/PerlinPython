# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2018-09-24 23:56:28
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2018-09-26 23:13:27

def testImportFunction():
	print("bonjour du 2eme fichier")

def printTheCloud(cloud):
	i = 0
	print("Dans la fonction printTheCloud\n  la fonction qui sert a ca specifiquement...")
	print("il y a ", len(cloud), " sous tableau(x)")
	for i in range (len(cloud)):
		print("  -> le ", i, "eme")
		print("   => avec ", len(cloud[i]), " lignes")
		j = 0
		for j in range (len(cloud[i])):
			print("    ==> et ", len(cloud[i][j]), " sous elements")
			print(cloud[i][j])
