#Create an EC2 ubuntu instance
#Allow TCP connections such as ssh (port 22), http (80) and https (4432)  and 8000
#Using ubuntu EC2 instance
sudo apt-get update
sudo apt-get upgrade 
sudo apt install gcc g++
sudo apt install mariadb-client-core-10.3
sudo apt-get install python3-pip

# Install the latest anaconda
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
sh Anaconda3-2020.02-Linux-x86_64.sh
source ~/.bashrc
conda init
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.python.sh | bash
sudo apt-get install git-lfs
sudo apt install mysql-client-core-8.0

# git ssh-keygen
  ssh-keygen -t rsa -b 4096 -C esseljojo1990@gmail.com
# Create the virtual environment


# Add conda to PATH
echo 'export PATH=path/to/anaconda/installation/bin:$PATH' >> ~/.bashrc
#eg echo 'export PATH=/home/ubuntu/anaconda3/bin:$PATH' >> ~/.bashrc

#pip install -r install_requirements.txt  --no-cache-dir


pip install fastapi SQLAlchemy uvicorn gunicorn  cryptography  PyMySQL mysql-connector-python
sudo apt install uvicorn -y
sudo apt install gunicorn -y

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