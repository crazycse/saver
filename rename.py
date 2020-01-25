t1='tea'
l=os.listdir(t1)
i=len(l)+1
for file in l:
  print(file)
  src=file
  dst=t1+str(i)+".jpg"
  os.rename(t1+'/'+src,t1+'/'+dst)
  i+=1
