#Mysql backup
#Author Vinay Gupta
DT=$(date +"%d%m%Y_%H%M%S")
mysqldump -uroot -pPASSWORD DB_NAME > /opt/DB_NAME_$DT.sql
gzip /opt/DB_NAME_$DT.sql
find /opt/ -name DB_NAME_* -type f -mtime +7 -exec rm {} \;
