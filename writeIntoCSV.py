# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2018-09-25 23:17:57
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2018-09-25 23:43:20

def writeToFile(cloud, nm):
	name = nm
	i = 0
	nm += ".csv"
	theFile = open(nm, "w+")
	print("in the write to file function")
	print("the cloud is compose of\n   ==> ", len(cloud))
	for i in range(len(cloud)):
		print("      -> at ", i, "position, we have ", len(cloud[i]), " numbers.")

	i = 0
	j = 0
	print(cloud)
	# print(cloud[0][0], "le zero zero")
	# for i in range(len(cloud)):
	# 	for j in range(len(cloud)):
	# 		print(cloud[i][j])
	# 		theFile.write(str(cloud[i][j]))
	# 		theFile.write(";")
	# 	j = 0
	# 	theFile.write("\n")
