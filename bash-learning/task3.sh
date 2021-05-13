#!/bin/bash
DATE=$(date +"%d-%m_%y")
HOSTNAME=$(hostname)

mkdir /tmp/$DATE

echo "Creating configuration backup files...."
for bkp in `ls /etc/*.conf`
do 
	echo "Backing up $bkp ..."
	CONFFILE=`basename $bkp`
	cp -p $bkp /tmp/${DATE}/$CONFFILE.bak

done

sleep 2
echo "Archiving the backup configuration files...."

tar -czf "/tmp/${HOSTNAME}-etc-backup-${DATE}.tar.gz" /tmp/$DATE  > /dev/null 2>&1 

sleep 3
rm -rf /tmp/$DATE
