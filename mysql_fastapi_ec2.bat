#Create an EC2 ubuntu instance
#Allow TCP connections such as ssh (port 22), http (80) and https (4432)  and 8000
#Using ubuntu EC2 instance
sudo apt-get update
sudo apt-get upgrade 
sudo apt-get install python3-pip


pip install fastapi SQLAlchemy uvicorn gunicorn  cryptography  PyMySQL mysql-connector-python
sudo apt install uvicorn
sudo apt install gunicorn

# Git clone the code from the repository
git clone -b BRANCH_NAME URL
# eg: git clone -b version1-scripts https://github.com/kaeflint/FastApiCoNomads.git


sudo apt install mariadb-client-core-10.3
# Make sure the Db is working well
mysql -h DB_URL -P 3306 -u USERNAME --password DB_PASSWORD

# Run the scripts to create the tables for the database


# Below is the connection string for the mysql connection
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://USERNAME:PASSWORD@HOST:3306/Database_Name"

# Run the code below to start the application
uvicorn application_main_filename:app --host 0.0.0.0 --port 8000