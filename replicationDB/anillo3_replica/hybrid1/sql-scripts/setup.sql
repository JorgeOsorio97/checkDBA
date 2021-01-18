-- MASTER REQUIREMENTS
CREATE USER IF NOT EXISTS 'repl1'@'%' IDENTIFIED BY '1234567890';

GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.*
TO 'repl1'@'%';


-- SLAVE REQUIREMENTS
CHANGE MASTER TO MASTER_HOST='hybrid2',
    MASTER_USER='repl2',
    MASTER_PASSWORD='1234567890',
    MASTER_LOG_FILE='bin-logs.000003',
    MASTER_LOG_POS=154;

START SLAVE;

