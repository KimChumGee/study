# 음식 배달 앱 (Food Delivery App)

일상 속 소프트웨어 사용 사례를 주제로 음식 배달 앱을 정함.

## 📁 폴더 구조

```
food_delivery_app/
├── food_delivery_app.py
├── menu_service.py
├── order_service.py
├── payment_gateway.py
```

# 응집도 / 결합도 평가 

각 모듈(`MenuService`, `OrderService`, `PaymentGateway`)은 하나의 책임만 갖도록 응집도를 높게 설계됨.
메인 앱은 서비스들의 인터페이스만 사용하며 결합도가 낮음.

# 시퀀스 다이어그램

아래는 이 앱의 흐름을 나타내는 시퀀스 다이어그램이다.

![시퀀스 다이어그램](diagram.png)
