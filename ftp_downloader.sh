#!/usr/bin/env bash 
echo $1
ftp_dir_adr=$1
curl -G $ftp_dir_adr | awk '{print $9}' > tmpdata
for dir in $(cat tmpdata); do
	path=$ftp_dir_adr
	path="$path$dir/"
	echo "$dir"
	echo $path | xargs curl -G -o "data/$dir"
	./ftp_downloader.sh $path
done
