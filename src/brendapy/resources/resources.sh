"""
Release of the latest resources.
"""
# data directory
cd src/brendapy/resources

# compress local data
DATA_ZIP="brendapy-data-v0.5.0.zip"
zip -r $DATA_ZIP data/

# upload data on server
scp $DATA_ZIP denbi-head:/var/www/html/brendapy

# restore data (for local development)
# rm $DATA_ZIP
cd brendapy
wget http://134.176.27.178/brendapy/$DATA_ZIP
unzip $DATA_ZIP
