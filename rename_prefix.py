import os
fil=[]
for r,d,f in os.walk("/home/vkchlt0334/animal/test/"):
	for files in f:
		fil.append(os.path.join(r,files))
for i in fil:
	base=os.path.split(i)
	basenam=os.path.basename(base[0])
	basename0=os.path.split(base[0])
	basenam1=os.path.basename(basename0[0])
	newname=basenam1+"_"+basenam+"_"+base[1]
	print(newname)
	count = 0
	file_count = 1
	new=os.path.join(base[0],newname)
	os.rename(i,new)
