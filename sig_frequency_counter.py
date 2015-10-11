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
	
	
	ind = np.arange(len(clnsigdict.values()))
	
	titles = {0: "Uncertain significance", 1: "Not provided", 2: "Benign", 3: "Likely benign", 4: "Likely pathogenic", 5: "Pathogenic", 6:"Drug response", 7: "Histocompatibility", 255: "Other"}
	height = clnsigdict.values()
	plt.bar(ind, height)
	plt.xlabel('Variant Clinical Significance type')
	plt.xticks(ind + 0.4, [titles[key] for key in clnsigdict.keys() ], rotation=-30)
	plt.ylabel('Frequency')
	plt.title(r'Distribution of mutations by Variant Clinical Significance type')
	plt.subplots_adjust(bottom=0.25)
	plt.show()


if __name__ == '__main__':
	main()
