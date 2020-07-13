#!/bin/bash

> oldFiles.txt

files="$(grep " jane " ../data/list.txt | cut -d " " -f 3)"

for i in $files;
do if test -e "/home/student-02-313d3b562e9f$i";
then echo "/home/student-02-313d3b562e9f$i" >> oldFiles.txt;
fi
done