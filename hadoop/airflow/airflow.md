## Airflow

### 가상환경 설정
```
virtualenv 3.9.10 airflow1
pyenv activate airflow1
```

### 설치
```
>pip install apache-airflow
```

### airflow 초기화
```
>airflow db init
# 결과로 ls ~/.airflow 디렉토리가 생성되어야함

# 만약 실패했을 경우
pip install kubernetes
pip install apache-airflow[cncf.kubernetes]
```

### 환경변수 설정
```
>gedit ~/.bashrc

export AIRFLOW_HOME=/root/airflow

>source ~/.bashrc
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
>airflow users create \
--username asdf \
--firstname K \
--lastname TH \
--role Admin \
--password 1234 \
--email asdf@example.com

# user 확인
>airflow users list

# 비밀번호 변경
>airflow users update --username your_username --password new_password


```
### standalone 실행
```
# 개발용으로 실행
# webserver, scheduler, metadata
airflow standalone

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
>gedit ~/airflow/airflow.cfg

# True를 False로 바꾸기
load_examples = False

```
--- 
---
## mysql 연동
```
# mysql 실행
>mysql -u root -p

# database 생성
create database airflow;

# root유저에 airflowDB권한 부여하기
grant all privileges on airflow.* to 'root'@'localhost';

# 계정 확인
USE mysql;
SELECT Host, User, authentication_string FROM user;
```

airflow.cfg 설정
```
>gedit airflow/airflow.cfg

sql_alchemy_conn = mysql://root:root@localhost:3306/airflow
```

```
# airflow 초기화
>airflow db init

# 만약 ModuleNotFoundError: No module named 'MySQLdb' 가 나오면
>pip install mysqlclient

# error 
>sudo dnf install mysql-devel
>pip install mysql-connector-python

bashrc에 export LD_PRELOAD=/lib64/libstdc++.so.6 => 해결
```

airflow.cfg 설정을 변경하여 기존 계정이 사라짐 
- 계정 다시 만들기

### airflow 디렉토리 안에 dags/test.py 만들기
```
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'spidyweb',
    'retries': 0,
    'retry_delay': timedelta(seconds=20),
    'depends_on_past': False
}

dag_Spark_api = DAG(
    'dag_Spark_api_id',
    start_date=days_ago(2),
    default_args=default_args,
    schedule_interval='*/10 * * * *',
    catchup=False,
    is_paused_upon_creation=False,
)

cmd="echo 'test succeed'"

#시작을 알리는 dummy
task_start = DummyOperator(
    task_id='start',
    dag=dag_Spark_api,
)
test_task = BashOperator(
    task_id='test',
    dag=dag_Spark_api,
    bash_command=cmd,
)

#의존관계 구성
task_start >> test_task
```

cd /etc/systemd/system
sudo nano airflow-webserver.service
```

```

