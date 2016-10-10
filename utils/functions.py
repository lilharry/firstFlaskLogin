#! /usr/bin/python


def genDic():
	x = open("data/info.txt").readlines()
	info = {}	
	for line in x:
		d = line.split(',')
		info[d[0]] = d[1].strip("\n")
	return info
	
def write(user,password):
	x = open("data/info.txt",'a')
	x.write(user + ',' + password + '\n')
	return 1