# 음식 배달 앱 (Food Delivery App)

이 프로젝트는 CLI 기반의 음식 배달 시뮬레이션 앱입니다.  
사용자는 메뉴를 조회하고, 주문하고, 결제를 진행할 수 있습니다.

## 📁 폴더 구조

```
food_delivery_app/
├── food_delivery_app.py
├── menu_service.py
├── order_service.py
├── payment_gateway.py
```

## ▶ 실행 방법

```bash
python food_delivery_app.py
```

# 응집도 / 결합도 평가 

각 모듈은 하나의 책임만 갖도록 고응집으로 설계됨.
메인 앱은 서비스들의 인터페이스만 사용하며 결합도가 낮음.

# 시퀀스 다이어그램

아래는 이 앱의 흐름을 나타내는 시퀀스 다이어그램입니다.

![시퀀스 다이어그램](diagram.png)
