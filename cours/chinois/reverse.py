# -*- coding: utf-8 -*-

def m():
  a=open("nombre 1-10.txt")
  b=a.readlines()
  a.close()

  a=open("rever.txt","w")
  mot={}
  for x in b:
##    #c=x.split(":")
##    for codec in ["utf-8","ISO-8859-15","utf-16",""]:
##                try:
##                      j=x.replace("\n","").decode(codec)
##                      u=j.split(":")[1]
##                      v=j.split(":")[0]
##                      coco=codec
##                      break
##                except:
##                  pass
    ##mot[u]=v
    a.write(x.split(":")[1].replace("\n",'')+":"+x.split(":")[0]+"\n")


  
##  f=mot.keys()
##  f.sort()
##  print f[-1],mot[f[-1]]
##  for x in f:
##    #a.write(x.encode(coco)+":"+mot[x]+"\n")
##    a.write(b[0])
  a.close()
