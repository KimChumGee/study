class PaymentGateway:
    def process_payment(self, amount):
        print(f"[결제게이트웨이] {amount}원 결제를 요청합니다.")
        return True  # 항상 결제 성공 처리 (시뮬레이션)
