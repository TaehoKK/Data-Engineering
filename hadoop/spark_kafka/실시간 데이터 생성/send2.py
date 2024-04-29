from kafka import KafkaProducer
import numpy as np
from time import time,sleep
import os
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer = lambda v: json.dumps(v).encode('utf-8'))
count = 0
while True:
    producer.send('topic1',value=np.random.normal())    
    sleep(.5)
    count += 1
    if count % 10 ==0:
        print("topic1 producer..........") 