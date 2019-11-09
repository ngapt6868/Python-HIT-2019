def x(la):
	return true;
def main():
	n = int(input())
	a = list(map(int, input().split()))
	for i in range(0, n):
		lx = a[i]
		cx = 0
		while (lx):
			cx = cx * 10 + lx % 10
			lx = int(lx / 10)
		if (cx == a[i]):
			print(a[i])
	#print("0")

if _name_ == '_main_':
	main()
