from menu_service import MenuService
from order_service import OrderService
from payment_gateway import PaymentGateway

class FoodDeliveryApp:
    def __init__(self):
        self.menu_service = MenuService()
        self.order_service = OrderService()
        self.payment_gateway = PaymentGateway()

    def run(self):
        print("🍽️ 음식 배달 앱")
        
        # 1. 메뉴 조회
        menu = self.menu_service.get_menu()
        print("\n[메뉴 목록]")
        for idx, item in enumerate(menu, 1):
            print(f"{idx}. {item}")
        
        # 2. 사용자 선택
        choice = int(input("주문할 메뉴 번호를 입력하세요: "))
        if choice < 1 or choice > len(menu):
            print("❌ 잘못된 선택입니다.")
            return
        selected_item = menu[choice - 1]

        # 3. 주문 요청
        order_msg = self.order_service.create_order(selected_item)

        # 4. 결제 요청
        price = 15000  # 임의 가격
        if self.payment_gateway.process_payment(price):
            print(f"✅ {order_msg} 결제가 완료되었습니다.")
        else:
            print("❌ 결제 실패. 주문이 취소되었습니다.")

# 실행
if __name__ == "__main__":
    app = FoodDeliveryApp()
    app.run()
