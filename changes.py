#!/usr/bin/env python
import sys
import vcf
import matplotlib.pyplot as plt
import numpy as np
import re

clnsigdict = dict()

def main():
	filename = sys.argv[-1]
	print(filename)
	f = open(filename, "r")
	for line in f:
		m = re.search("CLNSIG=(\d+)", line)
		if not m:
			continue
		signif = int(m.group(1)) 
		clnsigdict[signif] = clnsigdict.get(signif, 0) + 1

	date = filename[15:23]
	year = date[0:4]
	month = date[4:6]
	day = date[6:8]
	f = open('freq_dates.tmp', 'a')
	keys = [0, 1, 2, 3, 4, 5, 6, 7, 255]
	data = " ".join([str(clnsigdict.get(key, 0)) for key in keys])
	f.write(year + " " + month + " " + day + " " + data + '\n')

if __name__ == '__main__':
	main()
