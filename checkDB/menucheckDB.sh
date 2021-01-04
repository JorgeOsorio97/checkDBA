systemctl status mysqld | grep "running" >> /dev/null 

date
if [ $? -eq 0 ] 
then 
	echo "BASE todo cool"
else
	echo "Base de datos caida"
fi
