## SPARK

### 환경변수 설정
```
getdit ~/.bashrc
```
```
export JAVA_HOME=/root/jdk1.8.0
export HADOOP_HOME=/root/hadoop

export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH

export SPARK_HOME=/root/spark
export PATH=$PATH:$SPARK_HOME/bin:$PATH

export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='lab --allow-root'
```
---
#### 언어별 spark 실행 application 확인
```
$SPARK_HOME/bin
```

#### jupyter lab install
jupyter notebook으로 pyspark 열기
```
gedit ~/.bashrc
```
```
export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='lab --allow-root'

export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='lab --allow-root'
```
```
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


