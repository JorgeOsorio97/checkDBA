echo "Dime el usuario de la base de datos:"
read user
echo "Dime la contrasena"
read pass

echo "Bases de datos disponibles:"
mysql -u $user --password=$pass -e 'show databases'

echo "Cual base de datos quieres respaldar?"
read db

mysqldump -u $user --password=$pass $db -y > /home/jorge/backups/$db/backup_`date  +"%Y-%m-%d_%H:%M"`.sql