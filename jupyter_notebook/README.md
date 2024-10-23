### jupyter notebook 가상환경에서 실행

conda update
```
conda update conda
conda update anaconda

```
anaconda prompt 실행

가상환경 리스트 확인
```
conda-env list
```

가상환경 생성 및 삭제
```
- python 버전 확인
python --version

conda create -n 가상환경이름 python=버전

conda remove --name 가상환경이름 --all
```

가상환경 활성화 및 비활성화
```
conda activate 가상환경이름

conda deactivate
```

가상환경 실행 상태에서 ipykernel, jupyter notebook 설치
```
pip install ipykernel
pip install jupyter notebook
```

kernel 연결 및 해제
```
python -m ipykernel install --user --name 가상환경이름 --display-name "커널출력이름"
- 커널출력이름은 jupyter notebook에서 보이게 될 이름

jupyter kernelspec uninstall "커널이름"
```

kernel list 확인
```
jupyter kernelspec list
```

jupyter notebook 실행
```
jupyter notebook
```

원하는 파일을 열고 kernel 탭에서 change kernel


### jupyter 테마 변경

```
- 터미널
conda install -c conda-forge jupyter_nbextensions_configurator
```

문법 강조 기능
```
!pip install jupyter_nbextensions_configurator jupyter_contrib_nbextensions

!jupyter contrib nbextension install --user​

!jupyter nbextensions_configurator enable --user
```

