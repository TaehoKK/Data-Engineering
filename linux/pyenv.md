## pyenv
- 서로 다른 파이썬 버전을 설치 가능
- 디렉토리별로 서로 다른 파이썬 환경을 설정

### git에서 .pyenv로 cloning
```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# pyenv 작동을 빠르게 해준다.
# 오류가 나도 pyenv는 정상적으로 작동한다.
cd ~/.pyenv && src/configure && make -C src 
```
---

### 환경변수 설정
```
gedit ~/.bashrc
```
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```
```
source ~/.bashrc
```


### 원하는 파이썬 버전을 적어준다
```
pyenv install 3.9.10
```
#### 만약 install이 안될 때
```
# C컴파일러 설치
sudo dnf install gcc

sudo dnf install -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel
```

### pyenv-virtualenv github을 내 .pyenv/plugins로 cloning
```
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
# 여기서 이미 $(pyenv root)으로 설정이 되어 있다.
```

### 가상환경
```
# 가상환경 만들기
pyenv virtualenv 3.8.12 py38

# activate
pyenv activate airflow1

# deactivate
pyenv deactivate airflow1

# delete
# 방법 1
pyenv uninstall airflow1
# 방법 2
pyenv virtualenv-delete airflow1
```

만약 터미널을 실행할 이런 문구가 나오면 ssh lcoalhost 실행
```
bash: pyenv: command not found...
bash: pyenv: command not found...
```

