service mysqld status | grep "running" >> /dev/null 
if [ $? -eq 0 ] 
then 
	echo "BASE todo cool"
	echo "BASE todo cool <br />" >> /var/www/html/index.html
else
	echo "Base de datos caida"
	echo "Base de datos caida <br />" >> /var/www/html/index.html
fi
