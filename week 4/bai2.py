n = int(input("Nhap vao so luong phan tu cua mang a: "))
m = int(input("Nhap vao so luong phan tu cua mang b: "))
a = []
b = []
c = []
for i in range(n):
    x = int(input())
    a.append(x)
for i in range(m):
    x = int(input())
    b.append(x)
for i in range(n):
    for j in range(m):
        if a[i] == b[j] and a[i] not in c:
            c.append(a[i])
            break
print(c)