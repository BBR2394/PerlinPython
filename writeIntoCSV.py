# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2018-09-25 23:17:57
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2018-09-25 23:43:20

def writeToFile(cloud, nm):
        name = nm
        x = 0
        numTab = len(cloud)
        nm += ".csv"
        theFile = open(nm, "w+")
        print("in the write to file function")
        print("the cloud is compose of\n   ==> ", len(cloud))
        for x in range(numTab):
                print("      -> at ", x, "position, we have ", len(cloud[x]), " numbers.")
                i = 0
                j = 0
                for i in range(len(cloud[x])):
                        for j in range(len(cloud[x][i])):
                                print(cloud[x][i][j])
                                theFile.write(str(cloud[x][i][j]))
                                theFile.write(";")
                        j = 0
                        theFile.write("\n")
