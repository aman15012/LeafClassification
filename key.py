import numpy as np
import os
from shutil import copy2


def makeFolders_CopyFiles():
	f = open('key','r')
	f2 = open('train','w')
	f3 = open('test','w')
	x = f.readlines()
	for i in range(1,len(x)):
		x[i] = x[i].split('\t')
		if not os.path.exists(x[i][0]):
			os.makedirs(x[i][0] + '-Test')
			os.makedirs(x[i][0])
		rangeList = x[i][-2].split('-')

		start = int(rangeList[0])
		end = int(rangeList[1])+1

		rangee = end - start
		mid = int(rangee*0.8)

		for j in range(start, start + mid):
			copy2('Leaves/' + str(j) + '.jpg', x[i][0] + '/')
			s = str(i) + '\t' + str(j) + '.jpg' + '\t' + x[i][0] + '/' + str(j) + '.jpg\n'
			f2.write(s)
		for j in range(start + mid, end):
			copy2('Leaves/' + str(j) + '.jpg', x[i][0] + '-Test/')
			s = str(i) + '\t' + str(j) + '.jpg' + '\t' + x[i][0] + '-Test/' + str(j) + '.jpg\n'
			f3.write(s)

		print(i)
	f2.close()
	f3.close()

makeFolders_CopyFiles()