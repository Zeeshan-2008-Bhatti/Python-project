x=1
while x<=10:
	print(x,"x 2 =",x*2)
	x+=1
	print("done")

end=int(input("Enter End table:"))
for i in range(2,end+1):
	for j in range(1,11):
		print(j,"x",i,"-=",j*i)
		print()