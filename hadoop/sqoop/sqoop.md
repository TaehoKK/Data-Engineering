## sqoop

### sqoop 설치
```
wget https://archive.apache.org/dist/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
```
---
### sqoop 환경변수 설정
```
gedit ~/.bashrc
```
```
export SQOOP_HOME=/root/sqoop
export SQOOP_CONF_DIR=/root/sqoop/conf
export PATH=$SQOOP
```
```
source ~/.bashrc
```
```
gedit sqoop/conf/sqoop-env.sh
```
```
cd root/sqoop/conf
23 export HADOOP_COMMON_HOME=/root/hadoop
24 export HADOOP_HOME=/root/hadoop
27 export HADOOP_MAPRED_HOM=/root/hadoop
33 export HIVE_HOME=/root/apache-hive-3.1.3
```

---
### sqoop-mysql

#### mysql connector 설치
```
wget https://downloads.mysql.com/archives/get/p/3/file/mysql-connector-java-5.1.46.tar.gz
cd mysql-connector-java-5.1.46/
mv mysql-connector-java-5.1.46-bin.jar ~/sqoop/lib
cd sqoopls
cp sqoop-1.4.7.jar ~/hadoop/share/hadoop/tools/lib/
```

#### commons lang 설치
```
wget https://mirror.navercorp.com/apache//commons/lang/binaries/commons-lang-2.6-bin.tar.gz
cd commons-lang-2.6/
cp commons-lang-2.6.jar ~/sqoop/lib/
cd sqoop/lib
mv commons-lang3-3.4.jar commons-lang3-3.4.jar.bak #백업 파일로 변경
```
#### mysql 테이블 생성 
```
# mysql>
create table widget(id int not null primary key auto_increment,
widget_name varchar(64) not null, price decimal(10,2), design_date DATE,
version int, design_comment varchar(100));

insert into widget values(null,'sprocket',0.25,'2024-03-12',1,'Connects two gizmos');
insert into widget values(null,'gizmo',4.00,'2024-03-11',4,null);
insert into widget values(null,'gadget',99.99,'1983-08-13',13,'Our flagship product');
```

mysql 새계정 생성] 
```
# mysql>
create user 'hadoopguide'@'localhost' identified by 'password';
```

mysql 권한 설정
````
# mysql>
grant all privileges on hadoopguide.* to 'hadoopguide'@'localhost';
flush privileges;
````

권한 확인
```
show grants for hadoopguide@localhost;
# mysql>
sqoop list-databases --connect jdbc:mysql://localhost/hadoopguide --username hadoopguide --P 
# mysql> show databases; 의 결과와 같다.
```
---
### MySQL -> HDFS로 데이터 이동
```
sqoop import --connect jdbc:mysql://localhost/hadoopguide --table widget -m 1 # 책내용

sqoop import --connect jdbc:mysql://localhost/hadoopguide --username hadoopguide --table widget --P -m 1

sqoop import --connect jdbc:mysql://localhost/hadoopguide --username hadoopguide --P --query "select * from widget order by id" -m 1
# query로 정렬

sqoop import --connect jdbc:mysql://localhost/hadoopguide --table test -target-dir /user/root/test --username hadoopguide --P -m 1
```
데이터 확인
```
hadoop fs -cat /user/root/test/part-m-00000
```

table 복사
```
create table tbl_target like test;
```
---
### HDFS -> MySQL로 데이터 이동
```
sqoop export --connection jdbc:mysql://localhost/hadoopguide --table  --export-dir /user/root/test/part-m-00000 -- username hadoopguide --password password
```
```
# titanic
sqoop export 
--connection jdbc:mysql://localhost/hadoopguide 
--table tbl_target --export-dir /user/root/test/part-m-00000 
--username hadoopguide 
--password password
```
