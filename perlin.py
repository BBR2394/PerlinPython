#!/usr/bin/env python3
import random

def main(x, y, color, step):
	cloud = []
	i = 0
	stepCounter = 2
	for j in range (y):
		cloud.append([])
		while i < x:
			#cloud[j].append(random.randrange(255))
			r = random.randrange(255)
			print(r)
			cloud[j].append(r)
			i += stepCounter
		i = 0

		print("bonjour")
	print(cloud)
	print("toto")

main(16, 10, 1, 4)
