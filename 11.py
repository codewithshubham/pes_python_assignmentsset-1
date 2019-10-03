print("Input 10 students marks ")
x=[]
sum=0
more_avg=0
less_avg=0
eql_avg=0
for i in range(0,10):
	x.append(input("Input marks : "))
	sum=sum+x[i]
avg=sum/10	
for i in x:
	print i
	if i < avg:
		less_avg+=1
	if i > avg:
		more_avg+=1
	if avg==i:
		eql_avg+=1
print("Average : %d "%avg)		
print("Less than Average : %d "%less_avg)
print("More than Average : %d "%more_avg)

	
