# -*- coding: utf-8 -*-

def main():
  a=open("grec.txt")
  b=a.readlines()
  a.close()

  c=b[0].split()
  y=[]
  mot={}
  d=0
  
  for u in c:
      u=str(u)
      u=unicode(u)
      print u
      if d%3==0:
        mot[u]=""
        v=u
      elif d%3==1:
        mot[v]=u
      d+=1


  a=open("dicoaA.txt","w")
  f=mot.keys()
  f.sort()
  for x in f:
    a.write(x[:-1]+":"+mot[x][:-1]+"\n")
  a.close()
