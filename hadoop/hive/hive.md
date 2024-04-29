## HIVE

### hive install
<https://hive.apache.org/general/downloads/>
```
tar -xzvf apache-hive-3.1.3-bin.tar.gz
```
Hive Version |	Java Version
- Hive 1.0 | Java 6
- Hive 1.1 |	Java 6
- Hive 1.2 |	Java 7
- Hive 2.x |	Java 7
- Hive 3.x |	Java 8
- Hive 4.x |	Java 8
---
### hive 환경변수 설정
(hadoop 환경변수 설정 후)
```
gedit ~/.bashrc
```
```

HIVE_HOME=/root/apache-hive-3.1.3-bin

export JAVA_HOME HADOOP_HOME HADOOP_CONF_DIR HIVE_HOME
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HADOOP_HOME/lib/native
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$HIVE_HOME/bin

source ~/.bashrc
```

```
# hive 디렉토리로 이동
cd apache-hive-3.1.3-bin

# hive-env.sh.template 파일 이름을 hive-env.sh로 변경
mv conf/hive-env.sh.template conf/hive-env.sh
```
```
# hive-env.sh 파일에 하둡 홈 경로 설정
gedit conf/hive_env.sh
```
```
HADOOP_HOME=/Users/hongtebari/Platform/hadoop-3.3.0
```

hive-site.xml 설정

```
gedit /hive-site.xml
```
---
```
# hive만 실행하고자 할 때
<?xml version="1.0" encoding="UTF-8"?>
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
```
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>javax.jdo.option.ConnectionURL</name>
        <value>jdbc:mysql://localhost:3306/metastore?createDatabaseIfNotExist=true&amp;serverTimezone=Asia/Seoul</value>
        <description>metadata is stored in a MySQL server</description>
    </property>
    <property>
        <name>javax.jdo.option.ConnectionDriverName</name>
        <value>com.mysql.cj.jdbc.Driver</value>
        <description>MySQL JDBC driver class</description>
    </property>
    <property>
        <name>javax.jdo.option.ConnectionUserName</name>
        <value>hive</value>
        <description>user name for connecting to mysql server</description>
    </property>
    <property>
        <name>javax.jdo.option.ConnectionPassword</name>
        <value>1234</value>
        <description>hivepassword for connecting to mysql server</description>
    </property>
</configuration>
```
javax.jdo.option.ConnectionURL: 
- JDBC 연결 URL을 지정합니다. 이 경우 MySQL 데이터베이스의 주소 및 포트 번호가 포함되어 있습니다.
- createDatabaseIfNotExist=true는 데이터베이스가 없는 경우 자동으로 생성하도록 지정합니다. serverTimezone=Asia/Seoul은 서버의 시간대를 지정합니다.

javax.jdo.option.ConnectionDriverName:
- JDBC 드라이버 클래스 이름을 지정합니다. 여기서는 MySQL의 JDBC 드라이버 클래스인 com.mysql.cj.jdbc.Driver를 사용합니다.
javax.jdo.option.ConnectionUserName:
- 데이터베이스에 연결할 사용자 이름을 지정합니다. 이 경우 사용자 이름은 hive입니다.

javax.jdo.option.ConnectionPassword:
- 데이터베이스에 연결할 때 사용되는 비밀번호를 지정합니다. 이 경우 비밀번호는 1234입니다.

---

hive guava 버전 확인
```
>$HIVE_HOME/lib| grep guav

# 결과
-rw-r--r--  1 root staff  2308517 10월 19  2019 guava-19.0.jar
-rw-r--r--  1 root staff   971309 10월 19  2019 jersey-guava-2.25.1.jar
```
```
>$HADOOP_HOME/share/hadoop/common/lib | grep guav

# 결과
-rw-r--r-- 1 hdfs hdfs 2747878  7월 29  2022 guava-27.0-jre.jar
-rw-r--r-- 1 hdfs hdfs 3362359  7월 29  2022 hadoop-shaded-guava-1.1.1.jar
-rw-r--r-- 1 hdfs hdfs    2199  7월 29  2022 listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
```

jdbc 설치
```
curl -o $HIVE_HOME/lib/mysql-connector-java-8.0.22.jar https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.22/mysql-connector-java-8.0.22.jar
```

guava 교체
```
# guavav version 확인
ls $HIVE_HOME/lib
ls $HADOOP_HOME/share/hadoop/hdfs/lib

# 기존 guava 제거
rm -rf $HIVE_HOME/lib/guava-19.0.jar
rm -rf $HADOOP_HOME/share/hadoop/hdfs/lib/guava-11.0.2.jar

# 새로운 guava 설치
wget https://repo1.maven.org/maven2/com/google/guava/guava/27.0-jre/guava-27.0-jre.jar 
mv guava-27.0-jre.jar $HADOOP_HOME/share/hadoop/hdfs/lib/
cp $HADOOP_HOME/share/hadoop/hdfs/lib/guava-27.0-jre.jar $HIVE_HOME/lib/
```
DerbyDB 시작
```
$HIVE_HOME/bin/schematool -initSchema -dbType derby
```
![image](https://github.com/TaehoKK/Data-Engineering/assets/150890899/e8d0c1d6-0ca6-41cd-8a75-bb41ced21e41)
위 처럼 나오면 성공

### hive 실행
```
cd $HIVE_HOME/bin
hive
```

---
### directory 생성
```
>bin/hdfs dfs -mkdir -p /tmp/hive
>bin/hdfs dfs -mkdir -p /user/hive/warehouse

# 쓰기, 실행 권한 부여
>bin/hdfs dfs -chmod g+w /tmp
>bin/hdfs dfs -chmod g+w /user/hive/warehouse
>bin/hdfs dfs -chmod 777 /tmp/hive

```
---
### HiveQL
```
# 
> hive
show tables;


CREATE TABLE employee (
    emp_id INT,
    emp_name STRING,
    emp_dept STRING,
    emp_salary FLOAT
);

INSERT INTO employ VALUES
(1, 'John Doe', 'Engineering', 50000.00),
(2, 'Jane Smith', 'Marketing', 60000.00),
(3, 'Bob Johnson', 'Sales', 55000.00);

SELECT emp_dept, AVG(emp_salary) AS avg_salary FROM employee GROUP BY emp_dept;

```


---
---


### ERROR
hive 실행 오류
- Name node is in safe mode

해결: namemode safemode 끄기
```
# namemode의 safemode 끄기
hdfs dfsadmin -safemode leave

# namemode의 safemode 강제로 끄기
hdfs dfsadmin -safemode forceExit

# safe mode 확인
hdfs dfsadmin -safemode get
```

HiveQL 오류
- FAILED: HiveException java.lang.RuntimeException: Unable to instantiate org.apache.hadoop.hive.ql.metadata.SessionHiveMetaStoreClient

해결: metastore 초기화 및 schema 초기화
```
>ls $HIVE_HOME/meta*
# 결과
No such file or directory

rm -rf $HIVE_HOME/metastore_db
cd $HIVE_HOME
schematool -initSchema -dbType derby

# 결과
Initialization script completed
schemaTool completed



```
