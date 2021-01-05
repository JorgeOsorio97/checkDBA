#!/bin/sh
echo "Que quieres hacer?"
echo "1.- Revisar status de bd"
echo "2.- Hacer un backup"
echo "3.- Restaurar base de datos"

read accion
if [ $accion -eq 1 ]
then
    echo "Revisando status del servicio de mysql"
    ../checkDB/menucheckDB.sh
elif [ $accion -eq 2 ]
then
    echo "Iniciando proceso de respaldo"
    ../backupDB/menuBackUp.sh
elif [ $accion -eq 3 ]
then
echo "Iniciando proceso de restauriación de la base de datos"
    ../restore/menurestore.sh
fi
