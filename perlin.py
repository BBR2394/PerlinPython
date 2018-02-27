#!/usr/bin/env python3
import random

MasterCloud = []

def extrapol(a, b, step):
	print("nothing yet")
	toAddToCloud = []
	for i in range(step):
		toAddToCloud.append(i)
	print("dans extrapole", toAddToCloud)


def cloudGen(x, y, color, currentStep):

	cloud = []
	i = 0
	for j in range (y):
		cloud.append([])
		while i < x:
			#cloud[j].append(random.randrange(255))
			r = random.randrange(255)
			print(r)
			cloud[j].append(r)
			if currentStep > 1 and i > 0:
				print("le cloud")
				print(cloud[0])
				print("c'est le ", i/currentStep,  " tours donc je vais extrapoler")
				print(i)
				print(j)
				print(cloud[j][int(i/currentStep)])
				res = extrapol(cloud[j][int(i/currentStep)], r, currentStep)
				#cloud.append
			i += currentStep
		i = 0
		print("bonjour y")
	print(cloud)
	print("toto")
	MasterCloud.append(cloud)

#step is for the master cloud 

def perlinsCloud(x, y, color, step):
	currentStep = 1
	for i in range (step):
		cloudGen(x, y, color, currentStep)
		currentStep += 1

	print("master cloud")
	print(MasterCloud)

	for j in range (step):
		print("Master cloud step : ", j)
		print(MasterCloud[j])

perlinsCloud(16, 10, 1, 2)
