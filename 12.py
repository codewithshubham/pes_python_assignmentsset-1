print("Input 5 numbers ")
x=[]
for i in range(0,5):
	x.append(input("Input marks : "))
max=x[0]
if(max<x[1]):
    max=x[1]
elif(max<x[2]):
    max=x[2]
elif(max<x[3]):
    max=x[3]
elif(max<x[4]):
    max=x[4]    
print max
