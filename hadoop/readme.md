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

  
### YARN
- Resource Management, Job Scheduling/Monitoring 수행
- Resource Manager: Master Daemon에서 구동, 클러스터들로의 자원 할당을 관리
- Node Manager: Slave Daemon에서 구동, 각 단일 노드의 Task 실행
- Application Master: 개별적인 응용에서 필요로 하는 자원과 Job에 대한 lifecycle을 관리, Node Manager와 함께 작동하며, 작업의 실행을 모니터링
- Container: 한 노드의 자원을 모아둔 패키지 (RAM, CPU, Network, HDD 등)
