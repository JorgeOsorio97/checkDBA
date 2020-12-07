import subprocess
import os
from datetime import datetime as dt

import pandas as pd

from util_db import WEEKDAYS

weekday = dt.today().weekday()

dbs =  pd.read_csv('data/{}.csv'.format(WEEKDAYS[weekday]))
dbs =  {i[1]['db'] for i in dbs.iterrows()}
dump_cmd = 'mysqldump --password=1234567890 {db}  > /home/jorge/backups/{db}/backup_`date  +"%Y-%m-%d_%H:%M"`.sql'

for db in dbs:
    temp = dump_cmd.format(db=db)
    print(temp)
    # process = subprocess.run(temp
    # print(process)
    # output, error = process.communicate()
    os.system(temp)