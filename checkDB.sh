systemctl status mysqld | grep "running" >> /dev/null 

date
if [ $? -eq 0 ] 
then 
	# echo "BASE todo cool"
	# date >> /var/www/html/index.html
	# echo "BASE todo cool <br />" >> /var/www/html/index.html
	python3 /home/ulises/exito.py
else
	echo "Base de datos caida"
	date >> /var/www/html/index.html
	echo "Base de datos caida <br />" >> /var/www/html/index.html
	python3 /home/ulises/error.py
fi
