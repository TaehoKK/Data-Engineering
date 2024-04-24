## HIVE

### hive install
<https://hive.apache.org/general/downloads/>
```
tar -xzvf apache-hive-3.1.3-bin.tar.gz
```
#### Hive Version |	Java Version
- Hive 1.0 | Java 6
- Hive 1.1 |	Java 6
- Hive 1.2 |	Java 7
- Hive 2.x |	Java 7
- Hive 3.x |	Java 8
- Hive 4.x |	Java 8
---
### hive 환경변수 설정
hive-env.sh.template 파일 이름을 hive-env.sh로 변경
```
cd apache-hive-3.1.3-bin
mv conf/hive-env.sh.template conf/hive-env.sh
```


hive-env.sh 파일에 하둡 홈 경로 설정
```
HADOOP_HOME=/Users/hongtebari/Platform/hadoop-3.3.0
```
hive-site.xml 설정

```
gedit /hive-site.xml
```
```
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
<property>
<name>hive.metastore.warehouse.dir</name>
<value>/user/hive/warehouse</value>
</property>
<property>
<name>hive.cli.print.header</name>
<value>true</value>
</property>
</configuration>
```

---
