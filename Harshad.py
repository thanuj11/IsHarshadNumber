


def Harshad(n):

	leng=str(n)
	leng1=int(leng)
	sum=0
	
	for i in range(len(leng)):
		sum=sum+ int(leng[i])
		# print(sum)
	if(leng1%sum == 0):
		return 'true'
	else:
		return 'false'

mylist=[]
for i in range(1,501):
	if(Harshad(i) == 'true'):
		mylist.append(i)
		
print(mylist)



		
