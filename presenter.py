#!/usr/bin/env python
import sys
import vcf
import matplotlib.pyplot as plt
import numpy as np
import re
from datetime import date

clnsigdict = dict()

def main():
	f = open("freq_dates.tmp", "r")
	keys = [0, 1, 2, 3, 4, 5, 6, 7, 255]

	dates = []
	values = []
	for line in f:
		data = map(int, line.split())
		cdate = date(data[0], data[1], data[2])
		dates.append(cdate)
		values.append(data[3:])

	ind = np.arange(len(dates))
	
	titles = {0: "Uncertain significance", 1: "Not provided", 2: "Benign", 3: "Likely benign", 4: "Likely pathogenic", 5: "Pathogenic", 6:"Drug response", 7: "Histocompatibility", 255: "Other"}
	
	for key in xrange(len(titles.keys())):
		if key == 7:
			plt.plot(ind, [value[key] for value in values], 'o-', color='cyan')
		elif key == 8:
			plt.plot(ind, [value[key] for value in values], 'o-', color='orange')
		else:
			plt.plot(ind, [value[key] for value in values], 'o-')

	plt.xlabel('Date')
	plt.xticks(ind, dates, rotation=90)
	plt.ylabel('Frequency')
	plt.title(r'Distribution of mutations by Variant Clinical Significance type over time')
	plt.subplots_adjust(bottom=0.25)
	plt.legend(titles.values(), ncol=3, fontsize="small")
	plt.show()


if __name__ == '__main__':
	main()
