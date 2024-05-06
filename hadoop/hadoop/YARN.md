### yarn 파일 수정
- 주요 속성
  - yarn.resourcenamager.hostname : resourcemanager 노드에 설정
  - yanr.nodemanager.hostname : nodemanager 노드에 설정
  - tarn.nodemanager.aux-services : nodemanager 호스트를 별도로 운영할 경우 지정
  - yarn.nodenamager.aux-serviceces.mapreduce_shufflw.class : 지정하지 않아도 됨
 
    
```
>hadoop/etc/hadoop/yarn-site.xml

<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
    </property>
</configuration>
```


### yarn 실행
```
>hadoop/sbin/yarn-start.sh
```

### yarn 확인
<localhost:8088>
