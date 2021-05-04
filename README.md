# DKU2021-SWCONT-DIET
# 1. 개요
단국대학교 2021학년도 오픈소스SW기여 식단관리 프로젝트 "확찐자"
<p align = "left"><img width="500" alt="스크린샷 2021-05-03 오후 1 15 56" src="https://user-images.githubusercontent.com/58714529/116840757-12d0e180-ac12-11eb-99c8-4d5facdcb7ad.png"></p>


### 소개자료
  + 제안서 : [구글 드라이브 링크](https://drive.google.com/file/d/1LfTj4FPZnsRKj3KEfHNykUqSv6Q9cVlG/view?usp=sharing) 
  + 진행 보고서 : [구글 드라이브 링크](https://drive.google.com/drive/folders/12ayZw1eldpn_dXnF4yztRKn8S99etzy7?usp=sharing) 


# 2. 구성요소
본 프로젝트는 다음 구성 요소로 구성 되어 있습니다.

## frontend

서비스 웹 프론트엔드 구성

개발언어 및 프레임워크
+ node.js
+ react
+ html
+ css
+ javascript
 
컴포넌트 구성


<img src = "https://user-images.githubusercontent.com/58714529/116842996-7ad6f600-ac19-11eb-9b7e-86b956ab186f.png" width="400px">


## backend

서비스 API, 공공 API 데이터 크롤링 및 수집 구현, 식단 추천 알고리즘 제공

개발언어 및 프레임워크
+ django
+ djangorestframework
+ python
+ java

데이터베이스 구조

<img width="300" alt="스크린샷 2021-05-04 오후 12 41 08" src="https://user-images.githubusercontent.com/58714529/116958593-204f9f80-acd6-11eb-8802-49c0a68dbac9.png">

  

## 프로젝트 설치

본 프로젝트 repository를 프로젝트를 설치하고자 하는 환경에 내려받습니다.
~~~
git clone http://github.com/siwon9898/DKU2021-SWCONT-DIET
~~~
### frontend 설치 및 준비

1. nodejs 설치

   - `nodejs 12` 이상의 nodejs를 시스템에 설치합니다.
   
2. jslint 설치

   - `jslint 1.2` 이상의 jslint를 시스템에 설치합니다.
   
3. vscode extension : live server 설치

   - vscode의 extension 중 `live server`을 시스템에 설치합니다.
  
4. 로컬 서버 동작 확인
  
   - vscode 우측 하단 `Go Live` 버튼을 누르거나, `⌘L ⌘O` 키를 연속으로 눌러 테스트용 로컬 서버가 잘 작동 되는지 확인합니다.
  
  
### backend 설치 및 준비

1. python3 및 라이브러리 설치

     - `Python 3.7`이상의 파이썬 인터프리터 및 `pandas`, `bs4` 라이브러리를 시스템에 설치합니다.
  
2. json 설치

     - `json`을 시스템에 설치 및 업데이트 합니다.
 
### 식품 영양 데이터 수집

`💡 식품 영양성분 데이터 수집 과정에서 모든 영양소를 추출 하는것이 아닌 일부 영양소 정보 만을 추출합니다`

1. 사전 parsing된 데이터베이스 자료 import(권장)
  
  사전 수집된 데이터베이스 `backend_and_parser` 자료를 import하여 `xml`형태로 바로 사용 할수 있습니다.
  `2021. 5. 4` 기준으로 식품 영양성분 약 12000개가 수집 되어 있습니다.
  
2. 직접 수집

 `📎 공공 데이터 API를 사용하기 위해 직접 개발계정 신청 및 승인을 받아야 하므로 본 과정은 다소 번거로울 수 있습니다 `

  한국 공공데이터 포털에 접속합니다.
  
  ~~~ 
  https://www.data.go.kr/
  ~~~
  
  수령한 고유 서비스 키를 서비스 url에 입력하여 xml 형태의 API를 확인합니다.
  
  ~~~
  http://apis.data.go.kr/1470000/FoodNtrIrdntInfoService/getFoodNtrItdntList?ServiceKey=/*YourServiceKey*/
  ~~~
  
  다음 명령어로 데이터를 xml 형태로 parsing 합니다.
  
  ~~~
  table = xml.loads(result.content)
  ~~~
  
  vscode 하단 terminal에 xml 형태의 data array가 출력된다면 성공!
  
  ### 2021.5.4 기준 frontend UI 설계
  
  <img width="500" alt="스크린샷 2021-05-04 오전 1 08 35" src="https://user-images.githubusercontent.com/58714529/116957708-7ff87b80-acd3-11eb-921b-5187e06d4740.png">
  
  <img width="300" alt="스크린샷 2021-05-04 오전 1 30 02" src="https://user-images.githubusercontent.com/58714529/116957712-81c23f00-acd3-11eb-8b84-2fedd2a72253.png">

<img width="500" alt="스크린샷 2021-05-04 오전 12 44 17" src="https://user-images.githubusercontent.com/58714529/116957713-825ad580-acd3-11eb-8ed0-f485803b04ba.png">

<img width="500" alt="스크린샷 2021-05-04 오전 12 45 58" src="https://user-images.githubusercontent.com/58714529/116957716-82f36c00-acd3-11eb-8275-d546778bb78c.png">

<img width="500" alt="스크린샷 2021-05-04 오전 12 54 57" src="https://user-images.githubusercontent.com/58714529/116957717-82f36c00-acd3-11eb-9d09-73c003a3a1cc.png">
  



  

  

