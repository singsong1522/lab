from decimal import Decimal
a1=Decimal(1.5)
print(a1)
a2=Decimal(1.4)
print(a2)
a3=Decimal(2.968)
print(a3)
a4=Decimal('2.968')
print(a4)
a5=Decimal(2968)*Decimal(0.001)-Decimal(2.968)
print(a5)
a6=Decimal(2968)*Decimal('0.001')-Decimal('2.968')
#為了避免計算出現誤差,數字用字串代替
print(a6)
print("-----------------------------------------")
from decimal import ROUND_HALF_UP, ROUND_HALF_DOWN,ROUND_HALF_EVEN
difits = [1.5,2.5,3.5,4.5]
rounds = [ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP]
for d in difits:
    for r in rounds:
        result = Decimal(Decimal(d).quantize(Decimal(1), rounding=r))
        print(f"{d} using {r} ==> {result}")

print("-----------------------------------------")
a7 = Decimal(2.5)
result7 = Decimal(a7.quantize(Decimal(1),
                              rounding=ROUND_HALF_UP))
print(a7, result7)

a8 = Decimal(3.5)
result8 = Decimal(a8.quantize(Decimal(1),
                              rounding=ROUND_HALF_UP))
print(a8, result8)