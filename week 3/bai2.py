a = []
b = []
for i in range(4):
    x = int(input())
    a.append(x)
for i in range(4):
    x = int(input())
    b.append(x)
dta = (a[2]-a[0])*(a[3]-a[1])
dtb = (b[2]-b[0])*(b[3]-b[1])
dt_trung = 0
if b[0]<a[2] and b[0]>a[0] and b[1]<a[3] and b[1]>a[1]:
    x1 = abs(a[2]-b[0])
    y1 = abs(a[3]-b[1])
    dt_trung = x1*y1
dt = dta+dtb-2*dt_trung
print(dt)