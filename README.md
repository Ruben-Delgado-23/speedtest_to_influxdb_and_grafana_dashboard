# Speedtest to influxdb and grafana dashboard

This system will set up a dashboard to monitor and track internet speed using free software: Python, the speedtest-cli library by Ookla, InfluxDB, and Grafana. This setup will run on RaspiOS on a Raspberry Pi 4. The Python script will consistently execute the Speedtest CLI application, restructure the output data, and send it to an InfluxDB database. InfluxDB will be connected to Grafana, allowing you to visualize and investigate this data.

## 1. Install Necessary Libraries:
   
Install the required libraries python and the speedtest-cli package
```
sudo pip install speedtest-cli influxdb
sudo apt-get install python3-pip
```

## 2. Speedtest Using Python:
Create a Python script that uses speedtest-cli to measure the internet speed and sends the data to InfluxDB.

## 3. Schedule the Script:
You can schedule this script to run at regular intervals to ensure continuous monitoring.

## 4. Setting Up InfluxDB:
 ### 1.Install InfluxDB on RaspiOS. 
 Follow InfluxDB’s official documentation for installation steps: Grafana Installation   Guide. https://docs.influxdata.com/influxdb/v2/install/?t=Linux
 ### 2. Create a database on InfluxDB
  Create a database where you will store your speedtest measurements.
 ```
  create database test
  use test
  create user admin1 with password 'admin123' with all privileges
  grant all privileges on test to admin1
```
## 5. Setting Up Grafana:
### 1.Install Grafana:
Install Grafana on your server. Follow Grafana’s official documentation for installation steps: https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/
Go to http://serverip:3000/
### 2.Add InfluxDB as a Data Source:
   Grafana, go to Configuration > Data Sources.
   Add a new data source, choose InfluxDB, and provide necessary details like URL and database name.
 
![image](https://github.com/Ruben-Delgado-23/speedtest_to_influxdb_and_grafana_dashboard/assets/139746600/ddeb39bd-341c-416a-a5d1-38cd3486fc6b)

  Add database name, user and password.
  
  ![image](https://github.com/Ruben-Delgado-23/speedtest_to_influxdb_and_grafana_dashboard/assets/139746600/d6839c8d-b398-4341-b706-e58cbcc11fec)

### 3. Create a Dashboard:
Create a new dashboard in Grafana.
Add a new panel and configure it to use the InfluxDB data source you created earlier.
You can use InfluxDB queries to visualize your internet speed data. For example, you can use a query like FROM defualt "speedtest"  SELECT field("upload") distinct() GROUP BY time($_interval)
FORMAT AS Time series, give it an ALIAS 

 ![image](https://github.com/Ruben-Delgado-23/speedtest_to_influxdb_and_grafana_dashboard/assets/139746600/954ddaf6-a47d-4ede-aecb-eab66aba9be6)

## 6. Running the script and confirm the data on Influxdb and Grafana
**Influxdb**
 ```
influx
use test
Using database test
select * from speedtest
 ```

![image](https://github.com/Ruben-Delgado-23/speedtest_to_influxdb_and_grafana_dashboard/assets/139746600/fa705235-6ffc-4246-ae0a-7e92032c237a)


**Grafana**
Dasboard

![image](https://github.com/Ruben-Delgado-23/speedtest_to_influxdb_and_grafana_dashboard/assets/139746600/9eb5b5b2-e3cf-41ef-a395-6572b73a1126)


 
