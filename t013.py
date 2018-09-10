#end 关键字用于在输出结尾处加上不同的字符
#a,b=b,a+b 从右往左运行，将a+b赋值给b,再将b赋值给a
#Fibonacci series: 斐波纳契数列
a=0
b=1
while b<1000:
	print(b,end=',')
	a,b=b,a+b
