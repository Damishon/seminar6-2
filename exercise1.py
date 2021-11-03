filename=input("File atyn engiz:")
try:
	file1=open(filename)
except:
	print('File cannot be opened')
	exit()

lines=file1.readlines()
new_list=[]
file2=open('output.txt','w')
for line in lines:
	if line.startswith("Message-ID:"):
		word=line[13:40]
		if word not in new_list:
			new_list.append(word)
			new_list.sort()
print(new_list)
file2.write(str(new_list))
file1.close()
