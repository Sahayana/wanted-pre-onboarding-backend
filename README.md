# wanted-pre-onboarding-backend
8월 원티드 프리온보딩 백엔드 인턴십 - 선발 과제

## 지원자 정보
 - 이름: 양금성
 - 메일: didrmatjd@gmail.com

## 스택
 - 언어: python
 - 프레임워크: Django, Django-rest-framework(DRF)
 - 인프라: AWS EC2, AWS RDS
 - 개발환경: Docker, docker-compose
 - 테스트도구: pytest, pytest-django, factory-boy
 - CI/CD: Github Action, AWS CodeDeploy, AWS CodePipeline

## 개발환경설정


```bash
# 가상 환경 활성화
$ pipenv --python 3.7.6
$ pipenv shell
```
```
# 패키지 설치
$ pipenv install
```
```
# 도커 실행
$ docker-compose up -d --build
```
```
# 테스트 실행
$ pipenv pytest
```

## 모델
![MODEL](https://github.com/Sahayana/django-celery-prac/assets/91467403/01e66c50-18fa-4057-ae59-f17f18574b46)


## 어플리케이션 실행 방법 및 API 명세

  - 엔드포인트: ~~http://ec2-3-39-0-83.ap-northeast-2.compute.amazonaws.com/~~ (서버종료)
  - Account: [API 명세](https://documenter.getpostman.com/view/21367981/2s9Xy3trWd)
  - Article: [API 명세](https://documenter.getpostman.com/view/21367981/2s9Xy3trWj)

## 개발상세
 - 과제 요구사항 모두 구현하였습니다.
 - TDD방식으로 개발하였습니다.
 - 비즈니스 로직 혼재를 피하기 위해 모델 관련 비즈니스 로직은 쿼리셋, 매니저 레벨에서 관리하고, 시리얼라이저는 validation 역할만 하며, 대부분의 로직은 View 단에서 작성합니다.
 - 코드 포맷팅으로 flake8, black 사용하며 pre-commit 등록하여 관리했습니다.
 - 로직에 주석 첨부하였습니다.
 - 과제 초기 AWS Elasticbeanstalk으로 배포하다가 EC2로 재배포하였습니다.
   - 환경을 강제로 종료하는 과정에서 배포 버전이 꼬여 EB 자체적으로 무한재배포하는 오류 발생

## 어플리케이션 데모 영상
  - [link](https://drive.google.com/file/d/1szvxFo5Yugr_3dNWpoDVJrpqK1OAwvMc/view?usp=sharing)
