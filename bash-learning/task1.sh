#!/bin/bash
echo "******************* Gathering System Info... ****************************"

which dmidecode > /dev/null
if [ "$?" -ne 0 ]; then
    echo "Error! dmidecode command not found!"
fi
   
OSNAME=`cat /etc/*release| grep ^NAME| cut -d= -f2`
OSVERSION=`cat /etc/*release| grep ^VERSION= |cut -d= -f2`
KERNELVERSION=`uname -r`
CPUCOUNT=`nproc`
TOTALMEM=`cat /proc/meminfo | grep MemTotal | awk -F" " '{print $2}'`
SYSMF=`sudo dmidecode | grep "System Information" -A1 | grep Manufacturer |cut -d: -f2`

touch /tmp/Server-details.log

echo "***$(date)*****" | tee  /tmp/Server-details.log
echo "OS NAME            : $OSNAME" | tee -a    /tmp/Server-details.log
echo "OS VERSION         : $OSVERSION"  |tee -a /tmp/Server-details.log
echo "Kernel Version     : $KERNELVERSION" |tee -a  /tmp/Server-details.log
echo "CPU COUNT          : $CPUCOUNT" | tee -a  /tmp/Server-details.log
echo "TOTAL MEMORY       : $TOTALMEM Kb" | tee -a /tmp/Server-details.log
echo "SYSTEM MANUFACTURER: $SYSMF" | tee -a /tmp/Server-details.log

echo "System Details present in file: /tmp/Server-details.log"
echo "*************************************************************************"




