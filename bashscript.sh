#!/bin/bash
NUMOFKEYS=$(wc -l < ~/Programs/list.csv)
let NUMOFKEYS--
echo $NUMOFKEYS
while IFS=, read -r field1 field2
do
	if [[ "$field2" == "primaryTitle" ]]; then
		continue
	fi
	echo "$field1 and $field2"
	yt-dlp ytsearch5:"$field2"
done < ~/Programs/list.csv
echo $field2
#yt-dlp ytsearch5:
