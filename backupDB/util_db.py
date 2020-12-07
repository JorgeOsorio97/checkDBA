import os
WEEKDAYS = ['monday','tuesday','wednesday','thursday','friday', 'saturday', 'sunday']


def get_dbs_size(conn):
    cur = conn.cursor()
    cur.execute("SELECT "
                "table_schema, "
                "ROUND(SUM(data_length + index_length) / 1024 / 1024, 5) AS 'DB Size in MB' "
                "FROM "
                "    information_schema.tables "
                "GROUP BY "
                "    table_schema;")
    return [{'db':x[0], 'size': x[1]} for x in cur]

def create_dir(db_name):
    os.system('mkdir /home/jorge/backups/{}'.format(db_name))

