date

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