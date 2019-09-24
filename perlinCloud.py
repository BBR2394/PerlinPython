# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2019-09-24 16:51:33
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-09-24 17:21:58

import random

class PerlinCloud:
	MasterCloud = []
	x = 0
	y = 0
	color = 0
	step = 0

	def __init__(self, givenX, givenY, givenColor, givenStep):
		self.MasterCloud = []
		self.x = givenX
		self.y = givenY
		self.color = givenColor
		self.step = givenStep
		print("J'ai créé un objet PerlinCloud : MasterCloud = ", self.MasterCloud, " x =  ", self.x, " y = ", self.y, " color = ", self.color, " step = ", self.step)

	#frv -> ici je doit faire l'extrapolation entre les deux valeur 
	#quand il y a un pas strictement superieur a 2
	#en -> here i have to extrapolate values between the two corner value
	#when the step is strickly higher than 2
	def extrapol(self, a, b, step):
		print("nothing yet")
		toAddToCloud = []
		for i in range(step):
			toAddToCloud.append(i)
			print("dans extrapole", toAddToCloud)


	def cloudGen(self, x, y, color, currentStep):
		cloud = []
		i = 0
		for j in range (y):
			cloud.append([])
			while i < x:
				#cloud[j].append(random.randrange(255))
				#i generate a rand number between 0 and 255 because 
				#	i code the color on only 8 bit
				#	and if it is B&W it is enough
				r = random.randrange(255)
				print(r)
				#put value in the cloud array
				cloud[j].append(r)
				if currentStep > 1 and i > 0:
					print("le cloud")
					print(cloud[0])
					print("c'est le ", i/currentStep,  " tours donc je vais extrapoler")
					print(i)
					print(j)
					print(cloud[j][int(i/currentStep)])

					print("ici je vais mettre res")
					#I am going to extrapolate the data when step > 2
					#print(extrapol(cloud[j][int(i/currentStep)], r, currentStep))
					toAddToCloud = []
					for p in range(currentStep):
						toAddToCloud.append(p)
					#for y in range(len(res)):
					print(toAddToCloud)
					#cloud.append
				i += currentStep
			i = 0
			print("bonjour y")
		print(cloud)
		print("toto")
		#i push my previous array in the global one
		self.MasterCloud.append(cloud)

		#in this function I am going to mix all the sub array to only one
		#	and if i remember corectly the algo, I'll get the perlin's cloud
		#mixAllTheCloud()

	#step is for the master cloud 
	#masterCloud store the perlin's cloud ;-)
	def perlinsCloud(self, x, y, color, step):
		currentStep = 1
		for i in range (step):
			self.cloudGen(x, y, color, currentStep)
			currentStep += 1
		print("master cloud")
		print(self.MasterCloud)
		for j in range (step):
			print("Master cloud step : ", j)
			print(self.MasterCloud[j])

def test():
	perlin = PerlinCloud(16, 10, 1, 5)
	perlin.perlinsCloud(16, 10, 1, 5)


test()