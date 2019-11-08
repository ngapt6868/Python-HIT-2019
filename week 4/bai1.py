n = int(input("Nhap vao so luong phan tu cua 2 mang : "))
a = []
b = []
c = []
for i in range(n):
    x = int(input())
    a.append(x)
for i in range(n):
    x = int(input())
    b.append(x)
for i in range(n):
    c.append(a[i]+b[i])
print(c)