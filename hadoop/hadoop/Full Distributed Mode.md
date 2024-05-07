### 공통 설정
```
- hadoop 파일 시스템에 사용할 디렉토리 생성
#mkdir /dfs
#chown -R root /dfs

- 방화벽 제거
- 원래는 port 하나 하나 설정해야
#systemctl stop firewalld
systemctl disable firewalld

- 호스트명 설정
gedit /etc/hosts

192.168.111.100 master
192.168.111.200 slave
```

---
### 고정 ip 설정
```
- networmanager 사용할 경우 (/etc/sysconfig/network-scripts) 가 비어있음
- NetworManager 활성 여부 확인
systemctl status NetworkManager

- ip 설정
nmcli con mod eth0 ipv4.addresses 192.168.1.2/24
nmcli con mod eth0 ipv4.gateway 192.168.1.1
nmcli con mod eth0 ipv4.dns "8.8.8.8 8.8.4.4"
nmcli con mod eth0 ipv4.method manual
nmcli con up eth0


- NetworkManager 사용하지 않을경우
- 고정 아이피 설정
gedit /etc/sysconfig/network-scripts/ifcfg-eth0

TYPE=Ethernet
BOOTPROTO=static
NAME=eth0
DEVICE=eth0
ONBOOT=yes
IPADDR=192.168.111.100
NETMASK=255.255.255.0
GATEWAY=192.168.111.100.2
DNS1=168.126.63.1

- 네트워크 재시작
systemctl restart network


```
