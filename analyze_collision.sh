#!/usr/bin/sh


files=()

while read file ; do
    files+=${file}
done < <(find log/ -name "*.xml" )

python3 analyze_collision.py ${files}
