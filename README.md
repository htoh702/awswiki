# 필기노트 공유 및 QnA 서비스(ACSWIKI) – Toy Project

개발 기간: 
2024.05.07 ~ 2024.05.14

개발환경: 
Docker, Kubernetes, Django, Next JS, MySQL, EFK

개발 인원: 
4명

맡은 역할: 
Django를 활용한 백엔드 개발, MySQL을 이용한 데이터 모델 설계 및 구축, Docker를 이용한 Dockerfile 작성 및 Docker Compose 구성, EFK를 이용하여 모니터링 구축

내용 요약:
공부하면서 정리한 필기노트를 공유하고 모르는 문제는 묻고 답할 수 있는 서비스입니다.  

---
 
구성도

<img width="446" alt="image" src="https://github.com/user-attachments/assets/6326076f-d46a-48b3-9dfe-4c2d1b21fd2b">

-	Kubernetes를 이용하여 컨테이너 관리
-	NameSpace를 이용하여 Front-end, Back-end, Database, Monitoring컨테이너를 구분
-	TLS 인증서를 발급하여 HTTPS 통신 적용
-	Ingress를 이용하여 Next.js와 Django pod로 로드밸런싱
-	Monitoring을 위해 Fluent-bit를 이용하여 Log 데이터를, MetricBeats를 이용하여 Metric 데이터를 수집
-	수집된 데이터들은 Elasticsearch에서 분석
-	분석된 데이터들은 Kibana에서 시각화
---
Monitoring
  
Log 데이터

<img width="215" alt="image" src="https://github.com/user-attachments/assets/58bba826-3561-4e13-8ebc-c94f775856d9">

Metric 데이터

<img width="207" alt="image" src="https://github.com/user-attachments/assets/5cf1c736-84c0-479c-b43a-5c0b6f589f21">
