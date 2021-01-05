echo "Desde que fecha quieres recuperar la base de datos?"
read start

find /var/lib/mysql/ -name 'binlog.[0-9]*' | sort | xargs mysqlbinlog --start-datetime="$start" | mysql -u root --pasword=1234567890