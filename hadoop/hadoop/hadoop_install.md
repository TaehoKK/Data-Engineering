## hadoop

---
### hadoop install

<https://hadoop.apache.org>: hadoop 주소

1. hadoop homepage -> download -> binary -> 주소
2. wget <다운주소>
- tar -xzvf <파일> : 파일 압축 풀기

---
### java 11 version download
- 이유: hadoop 3.4버전이 java 8 and 11를 지원한다.
- <https://cwiki.apache.org/confluence/display/HADOOP/Hadoop+Java+Versions> 

---
### 환경변수 설정
- JAVA_HOME: java가 설치된 디렉토리의 경로를 지정
- HADOOP_HOME: hadoop이 설치된 디렉토리의 경로를 지정
- $PATH: 어디서든 실행할 수 있는 디렉토리의 경로를 지정

```
>gedit ~/.bashrc
```
```
export JAVA_HOME=/root/jdk-11.0.21
export HADOOP_HOME=/root/hadoop
export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
```
```
>source ~/.bashrc
```


---
### hadoop 환경변수 설정

hadoop-env.sh
- hadoop의 디렉토리 경로를 설정
- JAVA_HOME: Hadoop이 Java를 실행할 때 사용할 Java 홈 디렉토리를 지정
- HADOOP_HOME: Hadoop이 설치된 디렉토리의 경로를 지정
- HADOOP_CONF_DIR: Hadoop 구성 파일이 위치한 디렉토리의 경로를 지정
```
>gedit hadoop-3.3.6/etc/hadoop/hadoop-env.sh
```
```
export JAVA_HOME=/root/jdk-11.0.21
export HADOOP_HOME=/root/hadoop
export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop

# 사용자 지정 환경변수
export HDFS_NAMENODE_USER=root
export HDFS_DATANODE_USER=root
export HDFS_SECONDARYNAMENODE_USER=root
export YARN_RESOURCEMANAGER_USER=root
export YARN_NODEMANAGER_USER=root

# 각 디렉토리 설정
export HADOOP_COMMON_HOME=${HADOOP_HOME}
export HADOOP_MAPRED_HOME=${HADOOP_HOME}
export HADOOP_HDFS_HOME=${HADOOP_HOME}
export YARN_HOME=${HADOOP_HOME}
export HADOOP_COMMON_LIB_NATIVE_DIR=${HADOOP_HOME}/lib/native
export HADOOP_OPTS="-Djava.library.path=${HADOOP_HOME}/lib/native"
```

---
core-site.xml
- fs.defaultFS: Hadoop의 기본 파일 시스템을 설정
- HDFS의 기본 주소를 <localhost:9000>로 설정
```
>gedit ./hadoop-3.3.6/etc/hadoop/core-site.xml
```
```
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

---
hdfs-site.xml
- dfs.replication: 파일을 HDFS에 저장할 때의 복제 수를 설정
- 1로 설정되어 있어서 파일을 한 번만 저장하고 복제하지 않음을 의미

```
gedit ./hadoop-3.3.6/etc/hadoop/hdfs-site.xml
```
```
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

--- 
### hadoop 실행
자신의 lcoalhost에 ssh(secure shell)연결
```
>ssh localhost

# 종료
>exit 
```

---
password skip
- ssh localhost로 접속할 때 password skip
```
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
```
---
namemode 초기화 및 HDFS 실행
```
./hadoop/bin/hdfs namenode -format
./hadoop/sbin/start-dfs.sh
# 잘 안되면 start-all.sh 실행

# node가 정상적으로 작동하는지 확인
jps
```

Hadoop cluster의 web interface port
<localhost:9870>

#### namemode를 초기화 하는 이유
- 이전에 저장된 파일 시스템 메타데이터와 데이터 블록들을 제거
- 새로운 클러스터 또는 구성 적용
- 시작 시 문제 해결: 이전 클러스터의 상태가 부정상으로 인해 네임노드가 시작되지 않을 때, 초기화를 통해 클러스터를 정상 상태로 복원


---
hadoop fs 명령어
```
# 파일 및 디렉토리 확인
hadoop fs -ls /user/
# 모든 자식 디렉토리 및 파일 확인
hadoop fs -ls -R /

# directory 생성
hadoop fs -mkdir /user

# 만약 상위 디렉토리가 존재하지 않으면 같이 생성
hadoop fs -mkdir -p /user/taeho/hadoop_edu/test 

# local에서 hdfs의 input 디렉토리로 파일 복사
hadoop fs -put etc/hadoop/*.xml input
```

--- 
### jps 때 datanode 실행 안될 때
- tmp 초기화
<https://yeo0.tistory.com/entry/Solution-Namenode-Format-%ED%9B%84-Datanode-%EA%B0%80-%EC%8B%A4%ED%96%89%EB%90%98%EC%A7%80-%EC%95%8A%EC%9D%84-%EB%95%8C-Datanode-process-is-not-runni>

