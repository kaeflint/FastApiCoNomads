from utils.db_app import executeSQLCommand
from utils.config import *
create_table_statement ="""
    
    /*!40101 SET @saved_cs_client     = @@character_set_client */;
    /*!50503 SET character_set_client = utf8mb4 */;
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
    /*!40101 SET character_set_client = @saved_cs_client */;

    
    CREATE TABLE IF NOT EXISTS `tb_users`(
    `id` int NOT NULL AUTO_INCREMENT,
    `username` varchar(255),
    `pswd` text,

    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
     /*!40101 SET character_set_client = @saved_cs_client */;
"""

executeSQLCommand(create_table_statement)

populate_with_admin_account = f"""
INSERT INTO `tb_users`(`username`,`pswd`) VALUES ({ADMIN_NAME},{ADMIN_PASSWORD});
"""

executeSQLCommand(populate_with_admin_account)
