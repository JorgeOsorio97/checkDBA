service mysqld status | grep "running" >> /dev/null 
if [ $? -eq 0 ] 
then 
	echo "BASE todo cool"
	echo "BASE todo cool <br />" >> /home/jorge/Desktop/index.html
else
	echo "Base de datos caida"
	echo "Base de datos caida <br />" >> /home/jorge/Desktop/index.html
fi
