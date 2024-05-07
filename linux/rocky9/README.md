rocky9 inatalling documentation
<https://docs.rockylinux.org/guides/installation/>

rocky9 홈페이지에서 iso 파일 다운

vmware player에서 iso파일 설치
- 처음부터 iso 설치하지말고 나중에 설정

networkmanager 확인
```
systemctl status NetworkManager
```

linux gui 설치
```
- gui list 확인
dnf group list

- root로 로그인
dnf update
dnf group install "Workstation"
systemctl set-default graphical
```

