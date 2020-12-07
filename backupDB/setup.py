#/usr/bin/python3
from functools import reduce

import mysql.connector as mc
import pandas as pd

from util_db import get_dbs_size, WEEKDAYS, create_dir

conn =  mc.connect(
    host="localhost",
    user="jorge",
    password="1234567890"
)

dbs = get_dbs_size(conn)

total_size = reduce(lambda acum, current: acum + current['size'], dbs, 0)
number_dbs = len(dbs)
avg_size = total_size/number_dbs


print('Tamaño total de la BD: {} MB'.format(total_size))
print('Existen {} bases de datos'.format(number_dbs))
print('Tamaño promedio de base de datos: {}'.format(avg_size))

dbs = sorted(dbs, key=lambda item: item['size'], reverse=True)
size_per_day = total_size/7
dbs_per_day = number_dbs/7

# print(dbs)

for i in range(7):
    db_day = pd.DataFrame([], columns=['db'])
    curr_size = 0
    curr_quan = 0
    while curr_size < avg_size and curr_quan < dbs_per_day and len(dbs)>0:        
        actualdb = dbs.pop(0)
        create_dir(actualdb['db'])
        # print(i,actualdb)
        temp_df = pd.DataFrame([[actualdb['db']]], columns=['db'])
        db_day = db_day.append(temp_df)
        # print(db_day)
        curr_size += actualdb['size']
        curr_quan += 1
    db_day.to_csv('data/{}.csv'.format(WEEKDAYS[6-i]), index=False)
