## SPARK
- SparkContext => RDD => transformation => action => 결과
- transformation ex) map, filter
- action ex) collect, count

### 환경변수 설정

```
cd spark/conf
cp spark-env.sh.template spark-env.sh
gedit spark-env.sh

export SPARK_DIST_CLASSPATH=$(~/hadoop-3.3.6/bin/hadoop classpath)
export JAVA_HOME=~/jdk1.8.0

# spakr 실행시 로그 레벨 설정 (필수 아님)
# FATAL, ERROR, WARN, INFO, DEBIG. TRACE 순서
cp log4j2.properties.template log4j.properties
gedit log4j.properties

rootLogger.level = INFO 를
rootLogger.level = WARN 으로 변경
```

보류
getdit ~/.bashrc

export JAVA_HOME=/root/jdk1.8.0
export HADOOP_HOME=/root/hadoop

export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH

export SPARK_HOME=/root/spark
export PATH=$PATH:$SPARK_HOME/bin:$PATH

export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='lab --allow-root'


---
### 언어별 spark 실행 application 확인
```
$SPARK_HOME/bin
```

### spark 실행
```
~/spark/sbin/start-all.sh
jps

# 결과: worker, master 존재
```

# pyspark 실행
```
# python install 먼저

~/spark/bin/pyspark
```

#### jupyter lab install
jupyter notebook으로 pyspark 열기
```
gedit ~/.bashrc

export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='lab --allow-root'

export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='lab --allow-root'

source ~/.bashrc
```
```
pip install jupyterlab
# pip install -y python3-pip
```
```
pyspark
# jupyter lab이 열림
```

#### spark 모니터링
<localhost:4040>
- 하나의 노드에 여러개의 컨텍스트가 실행되면 포트번호가 1씩 증가하면서 생성
- 4041, 4042, ...


