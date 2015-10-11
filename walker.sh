#!/bin/bash -e
for file in $(find . -name 'clinvar*[0-9].vcf'); do 
	./changes.py $file
done 
