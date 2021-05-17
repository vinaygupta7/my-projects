#!/bin/bash
echo "Enter filename to be checked in /tmp directory : "
read filename

if [ ! -z $filename ]; then
	echo "checking for file...."
	FILE=`basename $filename`
        if [ -f /tmp/${FILE} ];  then
		echo "${FILE} file already exists in /tmp!"
	else
		echo "${FILE} doesnot exist in /tmp!"
	fi
else
	echo "Please enter filename"
	exit 1
fi
