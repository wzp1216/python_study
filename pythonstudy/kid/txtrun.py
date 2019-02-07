import time
scale=50
print("start".center(scale//2,"-"))
pstart=time.perf_counter()
for i in range(scale+1):
	a='*'*i
	b='.'*(scale-i)
	c=(i/scale)*100
	dur=time.perf_counter()-pstart
	print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
	time.sleep(0.1)
print("\n"+"over!".center(scale//2,'-'))

