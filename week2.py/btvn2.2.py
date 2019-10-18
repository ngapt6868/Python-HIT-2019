a=int(input("Nhập cạnh a:"))
b=int(input("Nhập cạnh b:"))
c=int(input("Nhập cạnh c:"))
if b>a and b>c:
    print("max la: ", b)
elif c>a and c>b:
    print("max la: ", c)
else:
    print("max la: ", a)
P= a+b+c
print("Chu vi của tam giác la: ", P)
h=P/2
S=(h*(h-a)*(h-b)*(h-c))
import math
print("Diện tích của tam giác là: ", math.sqrt(S))


