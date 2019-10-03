name=["ab","dsd","dasdsad","ababab"]
key=(string)input("input name to find : ")
for i in name:
	if key in name[i]:
		print("%s is found" %key)
	else:
		print("%s is  not founf" %key)