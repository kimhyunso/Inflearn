def pay(method, amount):
    if method == "CARD":
        print(f"신용 카드로 {amount}원 결제합니다.")
    elif method == "BANK":
        print(f"계좌이체로 {amount}원 결제합니다.")
    elif method == "PAYPAL":
        print(f"페이팔로 {amount}원 결제합니다.")
    # 새로운 결제 수단이 생기면 여기를 또 고쳐야함

pay("CARD", 50000)
pay("BANK", 50000)

# 오버라이딩
class Payment:
    def pay(self, amount): # 부모는 껍데기(interface)만 제공
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"[신용카드] {amount}원 결제 승인 완료.")

class BankTransfer(Payment):
    def pay(self, amount):
        print(f"[계좌이체] {amount}원 이체 확인되었습니다.")

class Paypal(Payment):
    def pay(self, amount):
        print(f"[페이팔] {amount}원 송금 완료.")

class NaverPay(Payment):
    def pay(self, amount):
        print(f"[네이버페이] {amount}원 결제 완료.")

# 다형성이 구현된 객체를 이용한 결제
def process_payment(payment_method, amount):
    payment_method.pay(amount)

method1 = CreditCard()
process_payment(method1, 50000)

method2 = BankTransfer()
process_payment(method2, 50000)

method3 = NaverPay()
process_payment(method3, 50000)

# Duck Typing
class CryptoCurrency:
    def pay(self, amount):
        print(f"[비트코인] {amount}원 결제 완료")

method4 = CryptoCurrency()
process_payment(method4, 7000)

payment_methods = [method1, method2, method3, method4]
for method in payment_methods:
    process_payment(method, 50000)