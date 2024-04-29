from kafka import KafkaProducer
import numpy as np
from time import time,sleep
import os
import json
import random

with open('data.txt','r',encoding='utf-8') as f:
    words = f.read().splitlines()  
    
producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer = lambda v: json.dumps(v).encode('utf-8'))
count = 0
while True:    
    index = random.randint(0,len(words)-1)
    producer.send('topic2',value=words[index])    
    sleep(1)
    count += 1
    if count % 5 ==0:        
        print("topic2 producer..........")  