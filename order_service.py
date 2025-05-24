class OrderService:
    def create_order(self, item):
        print(f"[주문서비스] '{item}' 주문을 생성합니다.")
        return f"{item} 주문이 접수되었습니다."
