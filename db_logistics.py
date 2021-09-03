from utils.db_app import executeSQLCommand,create_engine
from utils.config import *

# Make sure the database exists
mysql_URL = "mysql+mysqlconnector://jojo89:Melody2Jason@localhost:3306"
mysql_engine = create_engine(mysql_URL,echo=True)
# Query for existing databases
existing_databases = mysql_engine.execute("SHOW DATABASES;")
# Create database if not exists
if DATABASE not in existing_databases:
    mysql_engine.execute("CREATE DATABASE IF NOT EXISTS {0}".format(DATABASE))
    print("Created database {0}".format(DATABASE))
# Results are a list of single item tuples, so unpack each tuple
existing_databases = [d[0] for d in existing_databases]
mysql_engine.execute(f'USE `{DATABASE}`;')

# Create the tables
executeSQLCommand("""
CREATE TABLE IF NOT EXISTS `places` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `description` text,
    `coffee` tinyint(1) DEFAULT '0',
    `wifi` tinyint(1) DEFAULT '0',
    `food` tinyint(1) DEFAULT '0',
    `lat` float DEFAULT '0',
    `lng` float DEFAULT '0',
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci; 
""",mysql_engine)

executeSQLCommand("""
CREATE TABLE IF NOT EXISTS `tb_users`(
    `id` int NOT NULL AUTO_INCREMENT,
    `username` varchar(255),
    `pswd` text,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci; 
""",mysql_engine)


populate_with_admin_account = f"""
INSERT INTO `tb_users`(`username`,`pswd`) VALUES ('{ADMIN_NAME}','{ADMIN_PASSWORD}');
"""

# 
executeSQLCommand(populate_with_admin_account,mysql_engine)
