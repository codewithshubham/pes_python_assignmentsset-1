x = "Hello_World "
print x
print ("Characters in %s are " %x)
for i in x:
    print i
first=x[0:5]
second=x[6:]
print("Printing %s 100 times using repeat operator ")
print(x*100)
print("Sub string of %s is " %x)
print first
print second
print("Concatination of %s and %s is %s" %(first ,second,first+second))
