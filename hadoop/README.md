
hive: <https://wikidocs.net/book/2203#google_vignette>

### hadoop daemon
- hadoop cluster에서 실행되는 여러 프로세스
- hadoop 시스템의 다양한 부분을 담당
- Namemode, Datanode, ResourceManager, Secondary Namemode 등

### hadoop cluster
- node = 하나의 컴퓨터, rack = 여러 개의 node
- cluster = 여러 개의 rack

### HDFS
- 여러 컴퓨터에서 데이터를 저장하는 분산형 파일 시스템
- 파일을 block으로 나누어 저장 (단순화)
- 데이터 유실 방지
- 데이터의 무결성 유지
- Namemode: master, Datanode: slave
### YARM
