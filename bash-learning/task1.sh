#!/bin/bash
echo "******************* Gathering System Info... ****************************"
sleep 3
OSNAME=`cat /etc/*release| grep ^NAME| cut -d= -f2`
OSVERSION=`cat /etc/*release| grep ^VERSION= |cut -d= -f2`
KERNELVERSION=`uname -r`
CPUCOUNT=`nproc`
TOTALMEM=`cat /proc/meminfo | grep MemTotal | awk -F" " '{print $2}'`
SYSMF=`sudo dmidecode | grep "System Information" -A1 | grep Manufacturer |cut -d: -f2`

touch /tmp/Server-details.log

echo "***$(date)*****" > /tmp/Server-details.log
echo "OS NAME            : $OSNAME"     >> /tmp/Server-details.log
echo "OS VERSION         : $OSVERSION"  >> /tmp/Server-details.log
echo "Kernel Version     : $KERNELVERSION" >> /tmp/Server-details.log
echo "CPU COUNT          : $CPUCOUNT" >> /tmp/Server-details.log
echo "TOTAL MEMORY       : $TOTALMEM Kb" >> /tmp/Server-details.log
echo "SYSTEM MANUFACTURER: $SYSMF" >> /tmp/Server-details.log

echo "System Details present in file: /tmp/Server-details.log"
echo "*************************************************************************"




