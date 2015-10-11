#!/usr/bin/env python
import sys
import vcf

def main():
	filename = sys.argv[-1]
	print(filename)
	vcf_reader = vcf.Reader(open(filename, 'r'))
	for record in vcf_reader:
		signif = record.INFO['CLNSIG']
		signif = (signif[0].split('|')[0]) 
		print(signif)


if __name__ == '__main__':
	main()
