import datetime
import json
import subprocess

dt = datetime.datetime.now()
dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")

uptime = subprocess.check_output('uptime').decode('utf-8')
results = uptime.split(' ')

feed_json = {"datetime": dt_str, 
             "load1": float(results[11]),
             "load15": float(results[13].strip())}

print(json.dumps(feed_json))
