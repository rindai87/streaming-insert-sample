import datetime
import json
import subprocess

from google.cloud import pubsub


dt = datetime.datetime.now()
dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")

uptime = subprocess.check_output('uptime').decode('utf-8')
results = uptime.split(' ')

feed_json = {"datetime": dt_str, 
             "load1": float(results[10]),
             "load15": float(results[12].strip())}

print(json.dumps(feed_json))

TOPIC_NAME = "[PUBSUB_TOPIC_NAME]"
pubsub_client = pubsub.Client()
topic = pubsub_client.topic(TOPIC_NAME)

data = json.dumps(feed_json).encode('utf-8')
message_id = topic.publish(data)

print("Message {} published.".format(message_id))
