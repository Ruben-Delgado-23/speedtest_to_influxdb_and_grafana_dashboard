import datetime
import speedtest
from influxdb import InfluxDBClient

# influx environment variables
ifuser = "admin"
ifpass = "admin123"
ifdb   = "test"
ifhost = "127.0.0.1"
ifport = 8086

# Client config connecting to influx
ifclient = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)

# timestamp for this measurement
time = datetime.datetime.utcnow()

# running speedtest using default server
s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()
results = s.results.dict()

# format the data as a single measurement for influx
influx_data = [
    {
        "measurement": "speedtest",
        "time": time,
        "fields": {
            "download": results["download"],
            "upload": results["upload"],
            "ping": results["ping"]
        }
    }
]

# Writing to influxdb the measurement
ifclient.write_points(influx_data)
