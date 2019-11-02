s = input("Nhập vào chuỗi : ")
a = ""
for i in range(len(s)) :
    if i%2==0:
        a+=s[i]
    else :
        a = s[i]+a
print(a)