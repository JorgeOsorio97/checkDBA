systemctl status mysqld | grep "running" >> /dev/null 

date
if [ $? -eq 0 ] 
then 
	echo "BASE todo cool"
	date >> /var/www/html/index.html
	echo "BASE todo cool <br />" >> /var/www/html/index.html
else
	echo "Base de datos caida"
	date >> /var/www/html/index.html
	echo "Base de datos caida <br />" >> /var/www/html/index.html
fi
