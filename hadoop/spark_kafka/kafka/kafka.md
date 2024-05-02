# kafka

### install
```
tar -xzf kafka_2.13-3.7.0.tgz

cd kafka_2.13-3.7.0
```

## 환경변수 설정

```
gedit kafka/config/server.properties
```
```
listeners=PLAINTEXT://:9092
```

### zookeeper 실행
```
bin/zookeeper-server-start.sh -daemon config/zookeeper.properties
```
### kafka 실행
```
bin/kafka-server-start.sh -daemon config/server.properties
```

### kafka 중지 권한 부여
```
chmod +x bin/kafka-server-stop.sh
bin/kafka-server-stop.sh
```

# 실시간 log
```
tail -f logs/*
```

# topic 생성
```
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3 --topic test
```

# topic 제거
```
bin/kafka-topics.sh --delete --bootstrap-server localhost:9092 --topic test
```

# topic 리스트
```
bin/kafka-topics.sh --list --bootstrap-server localhost:9092 
```

# topic 구조 확인
```
bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 
```

# 확인 경로
```
ls /tmp/kafka-logs/
```

# producer 생성: 메세지 전송
```
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test
```

# consumer 생성: 메세지 출력
```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```

# 전송
```
bin/kafka-console-producer.sh --topic test --bootstrap-server localhost:9092
```

# 출력 (testgroup)
```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test -group testgroup --from-beginning
```

# consumer 그룹 확인
```
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
```

# testgroup의 구조 확인
```
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group testgroup --describe
```

#  offset reset
```
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group testgroup --topic test --reset-offsets --to-earliest --execute
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group testgroup --topic test --reset-offsets --to-latest --execute
(가장 최근에 추가된 메시지부터 읽어오게 됩니다. 따라서 이 옵션을 사용하면 이전에 Consumer가 이미 소비한 메시지는 제외되고, 새로 추가된 메시지만 읽어오게 됩니다.)
```
