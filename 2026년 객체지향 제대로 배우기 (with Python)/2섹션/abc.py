class Payment:
    def pay(self, amount):
        pass

class NaverPay(Payment):
    def refund(self):
        print("환불 가능")

# 기능 구현 하지 않음
pay = NaverPay()
pay.pay(5000)

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"신용카드로 {amount} 결제 완료")

class KakaoPay(Payment):
    def refund(self):
        print("카카오페이 환불")

card = CreditCard()
card.pay(30000)

# kakao = KakaoPay() 런타임  에러