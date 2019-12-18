#Write a programm to append the one array to another array
a=[1,2,4,5,6]
b=[2,4,8,9,0]
d=[2,5,6,8,10,14,26]
for i in range(0,len(a)):
	b.append(a[i])
print"the array :", b
for j in range(0,len(d)):
	if (d[j]%2==1):
		a.append(d[j])
print "the new array:",a
