비밀번호 정책 확인
```
SHOW VARIABLES LIKE 'validate_password%';
```


비밀번호 정책 완화
```
SET GLOBAL validate_password.length = 4;
SET GLOBAL validate_password.mixed_case_count = 0;
SET GLOBAL validate_password.number_count = 0;
SET GLOBAL validate_password.special_char_count = 0;
SET GLOBAL validate_password.policy = LOW;


```
