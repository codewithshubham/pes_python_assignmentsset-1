num = int(input("Enter a number: "))
if num > 1:
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")    
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  
x=input("Input the value of n :")
for num in range(1,x):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)