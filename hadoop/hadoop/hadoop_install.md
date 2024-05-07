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

###
```
$ sudo dnf install openssh
$ sudo dnf install pdsh

```

---

### 환경변수 설정
- JAVA_HOME: java가 설치된 디렉토리의 경로를 지정
- HADOOP_HOME: hadoop이 설치된 디렉토리의 경로를 지정
- $PATH: 어디서든 실행할 수 있는 디렉토리의 경로를 지정

```
$gedit ~/.bashrc

export JAVA_HOME=/root/jdk-11.0.21
export HADOOP_HOME=/root/hadoop
export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH

$source ~/.bashrc
```

### 호스트 명 설정
```
$vi /etc/hosts
```

### ssh 설정
- namemode와 datanode간 접속 id/pw 스킵
- ssh localhost로 접속할 때 password skip
```
$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
$ chmod 0600 ~/.ssh/authorized_keys
```
---


---
### hadoop 환경변수 설정

hadoop-env.sh
- hadoop 환경변수 설정 파일
- hadoop의 디렉토리 경로를 설정
- JAVA_HOME: Hadoop이 Java를 실행할 때 사용할 Java 홈 디렉토리를 지정 (hadoop 3.x부터 설정 필요없음)
- HADOOP_HOME: Hadoop이 설치된 디렉토리의 경로를 지정
- HADOOP_CONF_DIR: Hadoop 구성 파일이 위치한 디렉토리의 경로를 지정
```
$gedit hadoop-3.3.6/etc/hadoop/hadoop-env.sh

export JAVA_HOME=/root/jdk-11.0.21
export HADOOP_HOME=/root/hadoop
export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop

- 사용자 지정 환경변수
export HDFS_NAMENODE_USER=root
export HDFS_DATANODE_USER=root
export HDFS_SECONDARYNAMENODE_USER=root
export YARN_RESOURCEMANAGER_USER=root
export YARN_NODEMANAGER_USER=root

- 각 디렉토리 설정
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
- 이외
  - hadoop.tmp.dir : 임시 디렉토리 설정 (모든 노드에 설정)
  - fs.trash.interval : 휴지통에 보관할 시간, 디폴트 0분 (namemode에 설정) 
  - fs.trash.checkpoint.interval : 휴지통 비우는 시간, 디폴트 0분 (namemode에 설정)
```
$gedit ./hadoop-3.3.6/etc/hadoop/core-site.xml

<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>

```

---
hdfs-site.xml
- 주요 속성
  - dfs.replicastion : 복제 수
  - dfs.namemode.name.dir : fsimage가 저장될 경로 (namemode에 설정)
  - dfs.namemode.edits.dir : edits(에디트 로그)가 저장될 경로 (namemode에 설정)
  - dfs.datanode.data.dir : 데이터 파일이 저장될 경로 (datanode에 설정)
  - dfs.namemode.checkpoint.dir : fsimage, edits 사본이 저장될 경로 (secondary namemode에 설정)
  - dfs.namemode.secondary.http-address : 보조네임노드 주소와 포트번호 지정, 디폴트는 0.0.0.0:50090 (namemode에 설정)
 
- 이외
  - dfs.hosts & dfs.hosts.exclude : 노드를 추가허간 제거할 때 사용하는 파일 (추가 할 호스트 또는 제거 할 호스트의 이름을 지정)의 경로, 절대경로로 지정 (namemode에 설정)

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

### datanode의 호스트 이름을 기록하는 파일
```
$ gedit $HADOOP_HOME/etc/hadoop/workers
```

--- 
### hadoop 실행
자신의 lcoalhost에 ssh(secure shell)연결
```
>ssh localhost

# 종료
>exit 
```

namemode 초기화 및 HDFS 실행
- fsimage가 초기화
- 기존 data block은 삭제 안됨
```
./hadoop/bin/hdfs namenode -format


# 만약 datanode가 안나오면 /tmp/hadoop-root/dfs/data 삭제
# namemode를 초기화하면 새로운 block pool id 생성하기 때문에 두 번 포멧하면 오류 발생


# 여기에 fisimge 파일 2개가 만들어지면 정상적인 format 완료
cd $HADOOP_HOME
ls /tmp/hadoop-root/dfs/name/current/

# 결과:
VERSION                      fsimage_0000000000000000000.md5
fsimage_0000000000000000000  seen_txid
```

node 실행
```
start-dfs.sh

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
HDFS 디렉토리 생성/권한 부여
```
hdfs dfs -mkdir -p /tmp/hive
hdfs dfs -mkdir -p /user/hive/warehouse
hdfs dfs -chmod g+w /tmp
hdfs dfs -chmod 777 /tmp/hive
hdfs dfs -chmod g+w /user/hive
hdfs dfs -chmod g+w /user/hive/warehouse
```

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
--- 
### 추가

로그 디렉토리
- cat $HADOOP_HOME/logs/hadoop-사용자-노드구분-호스트명.log 확인

네임노드의 fsimage 위치
- /tmp/hadoop-사용자명/dfs/name

데이터 위치
- /tmp/hadoop-사용자명/dfs/data
  


보조네임노드의 fsimage 사본이 저장되는 디렉토리
- /tmp/hadoop-사용자명/dfs/namesecondary
