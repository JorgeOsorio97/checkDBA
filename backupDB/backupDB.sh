date
nohup mysqldump --all-databases --password=1234567890 > /home/jorge/backups/backup_`date  +"%Y-%m-%d_%H:%M"`.sql

if [ $? -eq 0 ] 
then 
	echo "Backup correcto"
	date >> /var/www/html/index.html
	echo "Back up en base de datos <br />" >> /var/www/html/index.html
else
	echo "Error en backup"
	date >> /var/www/html/index.html
	echo "Error en backuBack up en base de datos <br />" >> /var/www/html/index.html
fi