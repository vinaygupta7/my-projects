#!/bin/sh
#########################################################################
#       Monitoring log file generation and deletion via inotify		#
#       Author: Vinay Gupta						#
#       Email: vinaygupta.cse@gmail.com					#
#########################################################################

#Directory to be monitored

MONITORDIR="/var/logs"
inotifywait -m -e CREATE -e DELETE  -r --timefmt '%F %T' --format '%T %w %e %f' "${MONITORDIR}" | while read NEWFILE
# -m --> monitor   ; -e events ; %f is filename  for rest check man pages.
do
        echo $NEWFILE >> /tmp/newfilelogs.log
done
