## Airflow

### 가상환경 설정
```
virtualenv 3.9.10 airflow1
```

### 설치
```
pip install apache-airflow
```

### airflow 초기화
```
airflow db init
# 결과로 ls ~/.airflow 디렉토리가 생성되어야함

# 만약 실패했을 경우
pip install kubernetes
pip install apache-airflow[cncf.kubernetes]
```

### 유저 계정 생성

```
airflow users create \ 
> --username {Login_ID} \
> --firstname {First_NAME} \ 
> --lastname {Last_NAME} \
> --role Admin \ 
> --password {Password} \
> --email {Email}


ex)
airflow users create \
--username asdf \
--firstname K \
--lastname TH \
--role Admin \
--password 1234 \
--email asdf@example.com

```

### webserver 실행
```
# 둘 중 하나 실행
airflow webserver --port 8080
airflow webserver
```

### Scheduler 실행
```
# 새로운 창에서 실
airflow scheduler
```

### webserver 실행 화면
<localhost:8080>

### example DAG 제거
```
gedit ~/airflow/airflow.cfg
```
```
# load_examples = True에서 False로 바꾸기
# 안사라졌으면 껐다 키기
```
--- 
## mysql 연동
```
# mysql 실행
>mysql -u root -p

# database 생성
create database airflow;

# root유저에 airflowDB권한 부여하기
grant all privileges on airflow.* to 'root'@'localhost';
```

airflow.cfg 설정
```
gedit airflow/airflow.cfg
```
```
sql_alchemy_conn = mysql://root:root@localhost:3306/airflow
```

