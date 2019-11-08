n = int(input("Nhap vao so luong phan tu cua mang a: "))
a = []
c = {}
maxx =0
ten = ""
for i in range(n):
    x = input()
    a.append(x)
b = set(a)
for i in b:
    c[i] = a.count(i)
sorted(c.values())
for i in c.keys():
    print(i)
    break