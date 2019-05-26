#!/bin/bash

DIR=/home/vinay/sandeep/
for i in $DIR/*.csv.gz
 do
  zcat $i |awk -FT 'BEGIN {print "DATE\t\tTIME\t\tPRIVATE\t\tPUBLIC\t\tDESTINATION"} {print $1" " $2}'  | awk -F, '{print $1"\t"$5"\t"$7"\t"$9}'
  sleep 2
done; 
