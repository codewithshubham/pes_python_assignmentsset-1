n1 = 0
n2 = 1
count=0
nterms=input("Enter the no of series")
while count < nterms:
       print("%d"%n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
	   count=count+1